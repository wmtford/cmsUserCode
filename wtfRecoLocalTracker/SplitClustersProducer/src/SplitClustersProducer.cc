// -*- C++ -*-
//
// Package:    SplitClustersProducer
// Class:      SplitClustersProducer
// 
/**\class SplitClustersProducer SplitClustersProducer.cc wtfRecoLocalTracker/SplitClustersProducer/src/SplitClustersProducer.cc

 Description: Split SiStrip clusters from overlap tracks

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  Marco Cardaci
//         Created:  Sun Sep 21 15:22:40 CEST 2008
//         Updated:  Sep 2009 (release 3.1.X) wtford
// $Id: SplitClustersProducer.cc,v 1.6 2009/11/04 00:46:17 wtford Exp $
//
//

// this class header
#include "wtfRecoLocalTracker/SplitClustersProducer/interface/SplitClustersProducer.h"

// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

//Data Formats
#include "DataFormats/Common/interface/DetSet.h"
#include "DataFormats/Common/interface/DetSetVector.h"
#include "DataFormats/Common/interface/DetSetVectorNew.h"
#include "DataFormats/SiStripCluster/interface/SiStripCluster.h"
#include "DataFormats/SiStripCluster/interface/SiStripClusterCollection.h"
#include "DataFormats/TrackerRecHit2D/interface/SiStripRecHit2DCollection.h"
#include "DataFormats/TrackerRecHit2D/interface/SiStripMatchedRecHit2DCollection.h"
#include "DataFormats/Common/interface/OwnVector.h"
#include "DataFormats/TrackerRecHit2D/interface/SiStripRecHit2D.h"
#include "DataFormats/TrackerRecHit2D/interface/ProjectedSiStripRecHit2D.h"
#include "DataFormats/TrackerRecHit2D/interface/SiStripMatchedRecHit2D.h"
#include "DataFormats/SiStripDetId/interface/StripSubdetector.h"
#include "DataFormats/SiStripDetId/interface/TIBDetId.h"
#include "DataFormats/SiStripDetId/interface/TOBDetId.h"
#include "DataFormats/SiStripDetId/interface/TECDetId.h"
#include "DataFormats/SiStripDetId/interface/TIDDetId.h"

// For Pixel RecHits
#include "DataFormats/TrackerRecHit2D/interface/SiPixelRecHitCollection.h"
#include "DataFormats/TrackerRecHit2D/interface/SiPixelRecHit.h"

//TrackAssociator 
#include "SimTracker/TrackAssociation/interface/TrackAssociatorByHits.h"
#include "SimTracker/Records/interface/TrackAssociatorRecord.h"
 
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/ESHandle.h"

#include "DataFormats/GeometryVector/interface/LocalPoint.h"
//needed for the geometry:
#include "CommonTools/TrackerMap/interface/TrackerMap.h"
#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"  
#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"
#include "Geometry/CommonDetUnit/interface/GeomDetUnit.h"
#include "Geometry/TrackerGeometryBuilder/interface/StripGeomDetUnit.h"
#include "Geometry/TrackerGeometryBuilder/interface/StripGeomDetType.h"
#include "Geometry/CommonTopologies/interface/StripTopology.h"
#include "Geometry/CommonDetUnit/interface/GeomDetType.h" 

#include "AnalysisDataFormats/SiStripClusterInfo/interface/SiStripClusterInfo.h"
#include "DataFormats/DetId/interface/DetId.h"

#include "SimDataFormats/TrackerDigiSimLink/interface/StripDigiSimLink.h"

//For PSimHit

//#include "SimDataFormats/TrackingHit/interface/PSimHit.h"
//#include "SimDataFormats/TrackingHit/interface/PSimHitContainer.h"



#include "TFile.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TH2I.h"

//
// member functions
//

// ------------ method called to produce the data  ------------
void
SplitClustersProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

 using namespace edm;
 // using namespace reco;
 using namespace std;

  /*Marco*/
  trackerContainers.clear();
  cf_simhit.clear();
  cf_simhitvec.clear();

  //
  // Take by default all tracker SimHits
  //
  trackerContainers.push_back("g4SimHitsTrackerHitsTIBLowTof");
  trackerContainers.push_back("g4SimHitsTrackerHitsTIBHighTof");
  trackerContainers.push_back("g4SimHitsTrackerHitsTIDLowTof");
  trackerContainers.push_back("g4SimHitsTrackerHitsTIDHighTof");
  trackerContainers.push_back("g4SimHitsTrackerHitsTOBLowTof");
  trackerContainers.push_back("g4SimHitsTrackerHitsTOBHighTof");
  trackerContainers.push_back("g4SimHitsTrackerHitsTECLowTof");
  trackerContainers.push_back("g4SimHitsTrackerHitsTECHighTof");
  //  trackerContainers.push_back("g4SimHitsTrackerHitsPixelBarrelLowTof");
  //  trackerContainers.push_back("g4SimHitsTrackerHitsPixelBarrelHighTof");
  //  trackerContainers.push_back("g4SimHitsTrackerHitsPixelEndcapLowTof");
  //  trackerContainers.push_back("g4SimHitsTrackerHitsPixelEndcapHighTof");
 
  for(uint32_t i = 0; i< trackerContainers.size();i++){
    iEvent.getByLabel("mix",trackerContainers[i],cf_simhit);
    cf_simhitvec.push_back(cf_simhit.product());
  }
  
  std::auto_ptr<MixCollection<PSimHit> > allTrackerHits(new MixCollection<PSimHit>(cf_simhitvec));
  TrackerHits = (*allTrackerHits);
  /*Marco*/

 /////////////////////////
 // Cluster collections //
 /////////////////////////
 Handle< edmNew::DetSetVector<SiStripCluster> > dsv_SiStripCluster;
 iEvent.getByLabel("siStripClusters", dsv_SiStripCluster);

 /////////////////////////
 // RecHits collections //
 /////////////////////////
 edm::Handle<SiStripMatchedRecHit2DCollection> rechitsmatched;
 edm::Handle<SiStripRecHit2DCollection> rechitsrphi;
 edm::Handle<SiStripRecHit2DCollection> rechitsstereo;
 edm::Handle<SiPixelRecHitCollection> pixelrechits;
 iEvent.getByLabel("siStripMatchedRecHits","matchedRecHit", rechitsmatched);
 iEvent.getByLabel("siStripMatchedRecHits","rphiRecHit", rechitsrphi);
 iEvent.getByLabel("siStripMatchedRecHits","stereoRecHit", rechitsstereo);
 iEvent.getByLabel("siPixelRecHits",pixelrechits);
 hitAssociator = new TrackerHitAssociator(iEvent);

 /*Marco*/
 iEvent.getByLabel("simSiStripDigis", stripdigisimlink);
 /*Marco*/

 edm::ESHandle<TrackerGeometry> tkgeom;
 iSetup.get<TrackerDigiGeometryRecord>().get( tkgeom );

 // LOOP on DetSetVector<SiStripCluster> to get cluster and fill the split ones
 int iclusCnt = 0;
 auto_ptr< edmNew::DetSetVector<SiStripCluster> > splitSiStripClusters(new edmNew::DetSetVector<SiStripCluster>());
 splitSiStripClusters->reserve(10000,4*10000); //FIXME
 // Loop over subdetectors
 for(edmNew::DetSetVector<SiStripCluster>::const_iterator DSViter=dsv_SiStripCluster->begin(); DSViter != dsv_SiStripCluster->end(); DSViter++ ) {

  iclusCnt += DSViter->size();
  
  /*Marco*/
  uint32_t detID=DSViter->id();
  edm::DetSetVector<StripDigiSimLink>::const_iterator isearch = stripdigisimlink->find(detID);
  /*Marco*/

  edmNew::DetSetVector<SiStripCluster>::FastFiller ssc(* splitSiStripClusters, DSViter->id());
  //if (ssc.empty()) ssc.abort();

  // insert the DetSet<SiStripCluster> in the  DetSetVec<SiStripCluster>

  // Traverse the clusters for this subdetector
  for(edmNew::DetSet<SiStripCluster>::const_iterator ClusIter= DSViter->begin(); ClusIter!=DSViter->end();ClusIter++) {
   const SiStripCluster* clust = ClusIter;
   associatedIdpr.clear();
   associatedA.clear();
   size_t splittableClusterSize = 0;
   if (splitBy == SplitClustersAlgos::byHits) {
     hitAssociator->associateSimpleRecHitCluster(clust, associatedA);
     splittableClusterSize = associatedA.size();
   } else if (splitBy == SplitClustersAlgos::byTracks) {
     hitAssociator->associateSimpleRecHitCluster(clust, associatedIdpr, associatedA);
     splittableClusterSize = associatedIdpr.size();
   } else cout << "SplitClustersProducer:  Invalid splitBy value" << endl;

   /*
   SiStripClusterInfo* clusterInfo = new SiStripClusterInfo(*clust, iSetup);
   const StripGeomDetUnit*_StripGeomDetUnit = dynamic_cast<const StripGeomDetUnit*>(tkgeom->idToDetUnit(DetId(detid)));
   const StripTopology &topol=(StripTopology&)_StripGeomDetUnit->topology();
   MeasurementPoint mp(clusterInfo->baryStrip(),rnd.Uniform(-0.5,0.5));
   LocalPoint localPos = topol.localPosition(mp);
   float pitch = topol.localPitch(localPos);
   delete clusterInfo;
   */



      std::vector<uint8_t> amp=clust->amplitudes();

   // Fill the vector of SimHits associated with this Cluster

   /*Marco*/
//    if(splittableClusterSize == 2) {
   if(splittableClusterSize == 2 && amp.size()>1) {
   /*Marco*/

     // We have a cluster with more than one strip matched to at least 2 SimHits (or 2 SimTracks)

     /*
      float bary = clust->barycenter();
      cout << "Cluster barycenter:" << bary << endl;
      cout << "Cluster localPos:" << localPos << endl;
      cout << "Pitch:" << pitch << endl;
      const LocalPoint HitPosition = rechit.localPosition();
      float RecHit_x=HitPosition.x();
      float RecHit_y=HitPosition.y();
      float RecHit_z=HitPosition.z();
      cout << "---> RecHit_x:" << RecHit_x << endl;  
      cout << "RecHit_y:" << RecHit_y << endl;  
      cout << "RecHit_z:" << RecHit_z << endl;  
      for(vector<PSimHit>::const_iterator simhitsIter=associatedA.begin(); simhitsIter<associatedA.end(); simhitsIter++){
       int trackId = (*simhitsIter).trackId();
       PSimHit simHit =(*simhitsIter);
       float SimHit_x = (simhitsIter->entryPoint()).x();
       float SimHit_y = (simhitsIter->entryPoint()).y();
       float SimHit_z = (simhitsIter->entryPoint()).z();
//        float middlex = (simhitsIter->exitPoint().x() + simhitsIter->entryPoint().x() )/2.;
       float middlex = simhitsIter->localPosition().x();
//        float middley = (simhitsIter->exitPoint().y() + simhitsIter->entryPoint().y() )/2.;
       float h = middlex/pitch;
       cout << "SimHit_x in strips reference:" << h << endl;
       cout << "Difference:" << bary - h << endl;
       float SimHit_e = (*simhitsIter).energyLoss();
       cout << "---> SimHit_x:" << SimHit_x << endl; 
       cout << "SimHit_y:" << SimHit_y << endl;
       cout << "SimHit_z:" << SimHit_z << endl;
       cout << "simHit:" << simHit << endl;
       cout << "trackId:" << trackId << endl;
       cout << "SimHit_e:" << SimHit_e << endl;
       cout << "-----------------" << endl;
      }
    */


//   uint16_t stripCounter = leftStripCount(amp, associatedA, splitBy);
//   if(stripCounter > 0 && stripCounter < amp.size()) {

      /*Marco*/
//    std::cout << "New Cluster" << std::endl;
      int clusiz = amp.size();
      int first  = clust->firstStrip();
      int last   = first + clusiz;
      bool first_link = false;
      bool first_firstStrip1 = false;
      bool first_firstStrip2 = false;
      unsigned int trackID = 0;
      int first_CFpos = 0;
      std::vector<uint16_t> tmp1, tmp2;
      int firstStrip1 = 9999;
      int firstStrip2 = 9999;
      if(isearch != stripdigisimlink->end()) {
       edm::DetSet<StripDigiSimLink> link_detset = (*isearch);
//        cout << "detID = " << detID << endl;
       for(edm::DetSet<StripDigiSimLink>::const_iterator linkiter = link_detset.data.begin(); linkiter != link_detset.data.end(); linkiter++){
        if( (int)(linkiter->channel()) >= first  && (int)(linkiter->channel()) < last ){
	  int currentCFPos = linkiter->CFposition()-1;
	  int stripIdx = (int)linkiter->channel()-first;
	  uint16_t rawAmpl = (uint16_t)(amp[stripIdx]);
//  	  printf("%s%4d%s%5d%s%8d%s%8d%s%3d%s%8.4f\n", "CHANNEL = ", linkiter->channel(), " Ampl = ", rawAmpl,
// 		 " TrackID = ", linkiter->SimTrackId(), " CFPos-1 = ", currentCFPos, " Process = ",
// 		 TrackerHits.getObject(currentCFPos).processType(), " fraction = ", linkiter->fraction());
	 if (splitBy == SplitClustersAlgos::byHits) {
	  if (first_link == false) {
	    trackID = linkiter->SimTrackId();
	    first_CFpos = currentCFPos;
	    first_link = true;
	  }
	  uint16_t thisAmpl =  min((uint16_t)255, max((uint16_t)1, (uint16_t)(rawAmpl*linkiter->fraction())));
          if(currentCFPos == first_CFpos) {
	    if(linkiter->fraction()>0) tmp1.push_back(thisAmpl);
	    if(!first_firstStrip1) {
	      firstStrip1 = linkiter->channel();
	      first_firstStrip1 = true;
	    }
          } else {
	   if(linkiter->fraction()>0)
	     tmp2.push_back(thisAmpl);
           if(first_firstStrip2 == false) {
	     firstStrip2 = linkiter->channel();
	     first_firstStrip2 = true;
	   }
          }
	 } else if (splitBy == SplitClustersAlgos::byTracks) {
	   // (under construction)
	 } else {};
        }
       }
       SiStripCluster* newCluster1 = new SiStripCluster( clust->geographicalId(), firstStrip1, tmp1.begin(), tmp1.end() );
       SiStripCluster* newCluster2 = new SiStripCluster( clust->geographicalId(), firstStrip2, tmp2.begin(), tmp2.end() );
       if (firstStrip1 < first || firstStrip1 >= last || firstStrip2 < first || firstStrip2 >= last
	   || tmp1.size() <= 0 || tmp2.size() <= 0)
	 dumpSimTracks(hitAssociator, clust, newCluster1, newCluster2, splitBy);
       if(firstStrip1 != 9999 && tmp1.size() > 0) ssc.push_back(SiStripCluster( *newCluster1 ));
       if(firstStrip2 != 9999 && tmp2.size() > 0) ssc.push_back(SiStripCluster( *newCluster2 ));
      } else {
       std::vector<uint16_t> amp_temp;
       std::cout << "Missing digisimlink!!!" << std::endl;
       for(size_t j=0;j<amp.size();++j) amp_temp.push_back(amp[j]);
       SiStripCluster* newCluster = new SiStripCluster( clust->geographicalId(), clust->firstStrip(), amp_temp.begin(), amp_temp.end() );
       ssc.push_back(SiStripCluster( *newCluster ));
      } 

      // Make and store two clusters
      /*
       std::vector<uint16_t> tmp1, tmp2;
       for(size_t j=0;j<size_t(stripCounter);++j) tmp1.push_back(amp[j]);
       for(size_t k=size_t(stripCounter); k<amp.size(); ++k) tmp2.push_back(amp[k]);
       SiStripCluster* newCluster1 = new SiStripCluster( clust->geographicalId(), clust->firstStrip(), tmp1.begin(), tmp1.end() );
       SiStripCluster* newCluster2 = new SiStripCluster( clust->geographicalId(), clust->firstStrip()+tmp1.size(), tmp2.begin(), tmp2.end() );
//        dumpSimTracks(hitAssociator, clust, newCluster1, newCluster2, splitBy);
       ssc.push_back(SiStripCluster( *newCluster1 ));
       ssc.push_back(SiStripCluster( *newCluster2 ));
     

     } else {
	// One SimHit pulse height is << the other; just store the one cluster
       std::vector<uint16_t> amp_temp;
       for(size_t j=0;j<amp.size();++j) amp_temp.push_back(amp[j]);
       SiStripCluster* newCluster = new SiStripCluster( clust->geographicalId(), clust->firstStrip(), amp_temp.begin(), amp_temp.end() );
       ssc.push_back(SiStripCluster( *newCluster ));
     } 

     */

/*Marco-*/

   }else {
     // We don't have 2 SimHits; just store cluster in the output DetSetVector
     std::vector<uint16_t> amp_temp;
     for(size_t j=0;j<amp.size();++j) amp_temp.push_back(amp[j]);
     SiStripCluster* newCluster = new SiStripCluster( clust->geographicalId(), clust->firstStrip(), amp_temp.begin(), amp_temp.end() );
     ssc.push_back(SiStripCluster( *newCluster ));
   }
  }  // traverse clusters in subdetector
 }  // traverse subdetectors
 /*
 cout << "Number of initial clusters = " << iclusCnt << endl;
 int oclusCnt = 0;
 for(edmNew::DetSetVector<SiStripCluster>::const_iterator ODSViter=splitSiStripClusters->begin(); ODSViter != splitSiStripClusters->end(); ODSViter++ )   oclusCnt += ODSViter->size();
 cout << "Number of split clusters = " << oclusCnt << endl;
 */
 iEvent.put( splitSiStripClusters , "" ); 
 delete hitAssociator;
}

//
//  Find and dump simTracks associated with the original and new split clusters
//
void
SplitClustersProducer::dumpSimTracks(TrackerHitAssociator* hitAssociator, const SiStripCluster* origCluster,
				     const SiStripCluster* newCluster1, const SiStripCluster* newCluster2,
				     const int splitBy)
{
  std::vector<uint8_t> amp0 = origCluster->amplitudes();
//   if (amp0.size() < 4) return;
  std::vector<uint8_t> amp1 = newCluster1->amplitudes();
  std::vector<uint8_t> amp2 = newCluster2->amplitudes();
  if (splitBy == SplitClustersAlgos::byHits) {
    std::vector<PSimHit> simHitOrig;  simHitOrig.clear();
    std::vector<PSimHit> simHitNew1;  simHitNew1.clear();
    std::vector<PSimHit> simHitNew2;  simHitNew2.clear();
    hitAssociator->associateSimpleRecHitCluster(origCluster, simHitOrig);  cout << "-------------" << endl;
    hitAssociator->associateSimpleRecHitCluster(newCluster1, simHitNew1);  cout << "............." << endl;
    hitAssociator->associateSimpleRecHitCluster(newCluster2, simHitNew2);
    cout << "No. of simhits (orig, 1, 2): ";
    cout << simHitOrig.size() << ", " << simHitNew1.size() << ", " << simHitNew2.size();
  } else {  // byTracks
    std::vector<SimHitIdpr> simTkIdOrig;  simTkIdOrig.clear();
    std::vector<SimHitIdpr> simTkIdNew1;  simTkIdNew1.clear();
    std::vector<SimHitIdpr> simTkIdNew2;  simTkIdNew2.clear();
    hitAssociator->associateSimpleRecHitCluster(origCluster, simTkIdOrig);  cout << "-------------" << endl;
    hitAssociator->associateSimpleRecHitCluster(newCluster1, simTkIdNew1);  cout << "............." << endl;
    hitAssociator->associateSimpleRecHitCluster(newCluster2, simTkIdNew2);
    cout << "No. of simhits (orig, 1, 2): ";
    cout << simTkIdOrig.size() << ", " << simTkIdNew1.size() << ", " << simTkIdNew2.size();
  }
//   cout << ", widths:  " << amp0.size()
//        << ", " << amp1.size()
//        << ", " << amp2.size();
//   cout << ", first: " << origCluster->firstStrip();  cout << ", amps:" ;
  cout << ", first, width:  " << origCluster->firstStrip() << ", " << amp0.size() << " || "
       << newCluster1->firstStrip() << ", " << amp1.size() << " | "
       << newCluster2->firstStrip() << ", " << amp2.size() << endl << "  Amps:";
  for (size_t i=0; i<amp0.size(); ++i) cout << " " << int(amp0[i]);  cout << " ||";
  for (size_t i=0; i<amp1.size(); ++i) cout << " " << int(amp1[i]);  cout << " |";
  for (size_t i=0; i<amp2.size(); ++i) cout << " " << int(amp2[i]);  cout << endl;
  cout << "dumpSimTracks end ================================================================" << endl;
}

// ------------ method called once each job just before starting event loop  ------------
void 
SplitClustersProducer::beginJob(const edm::EventSetup&)
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
SplitClustersProducer::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(SplitClustersProducer);
