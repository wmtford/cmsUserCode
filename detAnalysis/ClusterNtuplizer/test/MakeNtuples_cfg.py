import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
duplCheck = cms.untracked.string('noDuplicateCheck')
source = cms.Source ("PoolSource",
                     fileNames = readFiles,
                     secondaryFileNames = secFiles,
                     skipEvents = cms.untracked.uint32(0),
#                     duplicateCheckMode = duplCheck
                     )

#readFiles.extend( [ 'file:cmsData/step2_RAW2DIGI_RECO_bugLink_defaultNoise_10.root' ] );
#secFiles.extend( [ 'file:cmsData/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_bugLink_defaultNoise_10.root' ] );

#readFiles.extend( [ 'file:cmsData/step2_RAW2DIGI_RECO_corLink_noNoise_100.root' ] );
#secFiles.extend( [ 'file:cmsData/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_corLink_noNoise_100.root' ] );

readFiles.extend( [ 'file:cmsData/step2_RAW2DIGI_RECO_corLink_1k.root' ] );
secFiles.extend( [
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_1.root',
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_2.root',
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_3.root',
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_4.root',
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_5.root',
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_6.root',
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_7.root',
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_8.root',
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_9.root',
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_10.root',
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_11.root',
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_12.root',
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_13.root',
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_14.root',
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_15.root',
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_16.root',
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_17.root',
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_18.root',
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_19.root',
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_20.root',
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_21.root',
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_22.root',
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_23.root',
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_24.root',
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_25.root',
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_26.root',
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_27.root',
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_28.root',
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_29.root',
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_30.root',
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_31.root',
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_32.root',
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_33.root',
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_34.root',
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_35.root',
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_36.root',
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_37.root',
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_38.root',
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_39.root',
'/store/user/wtford/trkHiDensity/QCD_Pt_3000_3500_cfi_corLink_CU/QCD_Pt_3000_3500_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_40.root'
                   ] );

#readFiles.extend( [
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_31X_V3-v1/0007/F8D2BBD0-CC78-DE11-A856-001D09F241D2.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_31X_V3-v1/0007/C4A3A5F2-E278-DE11-8B8A-001D09F25456.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_31X_V3-v1/0007/BAC269B7-CC78-DE11-83E5-001D09F29169.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_31X_V3-v1/0007/5C3EEAB4-CC78-DE11-A47B-001D09F290CE.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_31X_V3-v1/0007/56E7E9BC-CC78-DE11-B3FD-001D09F24D8A.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_31X_V3-v1/0007/4295B70E-D278-DE11-87D7-000423D6CA02.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_31X_V3-v1/0007/3C3597B3-CC78-DE11-998E-000423D98A44.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_31X_V3-v1/0007/3AD98805-CE78-DE11-AB1E-0019B9F7312C.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_31X_V3-v1/0007/34FBEBBE-CC78-DE11-B7BE-001D09F24637.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_31X_V3-v1/0007/28850C22-E978-DE11-90FC-001D09F252DA.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-RECO/MC_31X_V3-v1/0007/12CDCEC7-CC78-DE11-88D3-001D09F34488.root']);
#secFiles.extend( [
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/FE575692-CC78-DE11-8E27-001D09F2AF96.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/FC198C97-CC78-DE11-A7A4-001D09F241D2.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/F055C8A3-CC78-DE11-B539-000423D98BC4.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/D6C5D18A-CC78-DE11-A22D-001D09F29114.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/C2BDFDCA-CC78-DE11-AFC2-001D09F2447F.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/C08BBFB8-CE78-DE11-90DB-001D09F24664.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/ACB77B96-CC78-DE11-8C56-0019B9F72CE5.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/AC3183E7-CC78-DE11-A022-001D09F24024.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/A058F3C0-CC78-DE11-91E7-001D09F23A61.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/9EE73BA5-CC78-DE11-97F7-000423D8F63C.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/98818EB9-CC78-DE11-A4E1-001D09F24DDA.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/9691D28E-D278-DE11-BC29-000423D99394.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/94F7E9EE-E278-DE11-9B75-001D09F2516D.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/8AC868A1-CC78-DE11-B8AA-001D09F24664.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/867F88CE-D178-DE11-AF51-000423D9890C.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/84CA3C9A-CC78-DE11-B409-001D09F2532F.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/84C5E1A9-CC78-DE11-A283-0019B9F72F97.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/84B8D800-CD78-DE11-B2E0-000423D99E46.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/80A958A3-CC78-DE11-B4AF-000423D99F1E.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/7230EBA1-CC78-DE11-A023-001D09F251BD.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/7099D79E-CC78-DE11-ACBB-000423D98FBC.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/6E8C60C0-CC78-DE11-9258-001D09F2960F.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/62FBBAC6-CC78-DE11-9C88-001D09F251FE.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/60D47CC9-CC78-DE11-B203-001D09F23A07.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/5C501299-CC78-DE11-8C15-001D09F23A61.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/565584AA-CC78-DE11-ABA7-001D09F295FB.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/56120694-CC78-DE11-914B-0019B9F71A6B.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/50FD14A0-CC78-DE11-8F84-001D09F251FE.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/4891923D-D578-DE11-BBB5-000423D98868.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/400628A3-CC78-DE11-9424-000423D60FF6.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/3EAC289E-CD78-DE11-ADE0-001D09F24EAC.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/20D79C96-CC78-DE11-90F8-001D09F2915A.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/1E0A93BF-CC78-DE11-B57D-000423D98BC4.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/1C4946CA-CC78-DE11-AE0D-001D09F24EAC.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/1A09B692-CC78-DE11-AF45-001D09F248F8.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/1057C03A-D178-DE11-A339-000423D98EC4.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/0822DD24-E978-DE11-B43C-001D09F253C0.root',
#'/store/relval/CMSSW_3_1_2/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/MC_31X_V3-v1/0007/02AAD3A6-D078-DE11-9C9A-000423D98EC8.root']);

process = cms.Process("makeNtuple")
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.Services_cff")
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.load("SimGeneral.MixingModule.mixNoPU_cfi")

### conditions
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = 'MC_31X_V3::All'

process.load("SimTracker.Configuration.SimTracker_cff")
process.load("Configuration.StandardSequences.Reconstruction_cff")
process.load("Validation.TrackerDigis.trackerDigisValidation_cff")
process.load("SimTracker.TrackAssociation.TrackAssociatorByHits_cfi")
process.load("RecoTracker.TrackProducer.CTFFinalFitWithMaterial_cff")

process.load("RecoTracker.TrackProducer.TrackRefitters_cff")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1))
process.MessageLogger.cerr.FwkReport.reportEvery = 10
#process.MessageLogger.cerr.threshold = 'Info'
process.source = source

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('clusNtuple.root')
)

#process.Timing = cms.Service("Timing")
#process.SimpleMemoryCheck = cms.Service("SimpleMemoryCheck")
process.makeNtuple = cms.EDAnalyzer('ClusterNtuplizer'
)

process.rechits = cms.Sequence(process.siPixelRecHits*process.siStripMatchedRecHits)

#process.event = cms.EDAnalyzer("EventContentAnalyzer")
process.p1 = cms.Path(process.mix*process.rechits*process.TrackRefitter*process.makeNtuple)

