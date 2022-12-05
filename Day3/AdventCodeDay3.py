
def compare(a,b):
    for x in a:
        for y in b:
            if x == y:
                return x
    return 0

def compare3(a,b,c):
    for x in a:
        for y in b:
            for z in c:
                if x == y:
                    if x == z:
                        return x
    return 0


def char_position(letter):
    pos = ord(letter)
    if pos < 97:
        return pos - 65 + 27
    else:
        return pos - 96



compartments = []
itemCount = []
dupItems = []
pri = []

"""
sackArray = ['vJrwpWtwJgWrhcsFMMfFFhFp',
'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
'PmmdzqPrVvPwwTWBwg',
'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
'ttgJtRGJQctTZtZT',
'CrZsJsPPZsGzwwsLwLmpwMDw']


"""

sackArray = ['zBBtHnnHtwwHplmlRlzPLCpp',
'vvhJccJFGFcNsdNNJbhJsJQplQMRLQMlfdfTPCLfQQCT',
'GPhjcjhZDjWtnSVH',
'BNhHVhrGNVTbDHdDJdJRPJdSQQSJwPjR',
'lvtsfbsqzwSnJcvjSm',
'MftttFLftZMLgtgMbltMqZzbDNrTpVGhNWrDTrpTGNpZGZhD',
'VSSHcTgTtTdtllZlzmmbljTn',
'RqMqsFfQLLFLQFMMfRLPZLvPpCfWrbpmCbjCnfjlWmnrmmnm',
'hqRDqPDRsqNHwtHSNBZtJd',
'tNFDpDFrtdjfmjjjFmFFdScpZhZScTJgpHccHhMJgS',
'lLzSlSCQqbsVhBghggBZgCcJ',
'zRLVVLQnvQqVVzRldfWrwffjjdwSdfjv',
'bpWqqqWvHBpwGBCCRl',
'hJdjdJFQqdBBDMMC',
'tFFzJZFtJSqtZJQsWLbNSTnffHfvTH',
'lFhRZhFjPlqMlJqZJlJcRLwrLrwStRwtsVVtVSrgRV',
'WcpDvDfBmpDHzWBDbpbmWmNVSSTzLTtrVswgttVVzwwr',
'pbWfmGBpHfDmWnvvGbmWnjjMqPJMlMFPdGcjqPqPhP',
'NjFNRlpVLFCSSlbBWWfw',
'pssPZQQsMnzmtnQPttzDBbBJBcrrJWbrZSBJSbfC',
'QTHPHspMNGHdhvRR',
'QfPdSJfFJmthSthtwbsNLbPLlLTLpbvP',
'nHnMBnZqqgBMnWrZMqnZVcbCqRwNsvblRwppbllTsRNp',
'nZHBHznMnWgcrnVBtjFdfmzQNtNddjNF',
'hFhfPghppPhpRNhzsjsvHVzjpsGnWz',
'tTjlCCwMqtdMjMctGJWHwWnVwWnwvWGs',
'rZdrjBBtqdCtlcdgFZQLfhRLFSgRNP',
'RDHSWrJWffJFlJCgCMCDjCvzjPMP',
'QtGTndBwBtNzBVjBCMgB',
'LdwwMpTdwsRHsqSHqHJl',
'RfsfzvLLFvFzCSvSbDsTpTGMPMZPPTMt',
'jqWBjwBBNwWqwPGZbTwVwVtD',
'BnhgglhhNNngqjBjHNWrZLlFLSCJSFFCCQzQvQFCFF',
'HLvLDQbvnDQDvbHTLhntSnGBSlfGldddcmfMMf',
'NgFjZjrZZJrlfJfSVcBJGc',
'scWCNFZpsjzrDLwLhbQzhQwD',
'SlqJlThDPqpwSTwhcbDdbWDbZGcZNcDb',
'MsnWWjHjvLvfscjjgdzNdbgbcc',
'vQQvWVQFLLHfHVBWfsfmFFpJRhhSplqlRJqpBwlqTCPC',
'DZbDzzZDjQbPGZFFSSgSlFCzTgzm',
'qLnvwvhddrqMrwrCTLLFJjmtSlFlSH',
'VdhvsWqdVWvvRhsvqbpbPcZfPpjZGBQNRj',
'mJNtNFmzDZtzdzrLtwwRqJSchgfGcRfwRB',
'pWpjQjCTQnHMWCCpjQpHvTqcwTwScfRcBcSGBRThwS',
'MQHjvjVCCqsvljWnVQzLtNPZzmzLVNLddtPN',
'QVRPRVDgsRjLssnL',
'TTGDJDJfbfLHSnsMWWbs',
'qGqqTFFDqgQgQQQq',
'nlMnRRjbMjCdJVQJCZ',
'nGqfLwfNLFNLnPPGFVVCdVGZJtCtCCVzJz',
'LHHfPNHnPqqLwqPqDPWfNFvMglbhhbMgmclgcllDmgmrcl',
'cLLWWSThtdLpRcddcgPRZFDMCVPPMCCPCPCZ',
'NfGbGNzrBNffGNJjbPPZsZmZZPmDHpMH',
'zlJBfzlQzNjNjfJcpwSdvWhcvLwQWt',
'cVVQfVCJVrVcTJnfNvlDFmDrmlvrFWlL',
'snZHpMhZtMbtPNvzHWWvNFNvNW',
'gppnbbbRgMnZbswRqRwbqTcCCSTCJJdGjgfVGTdcCG',
'jplgNdrHrrNZgdHmlHNJHddlDSPPSTlzTSlTSDSzCQLfzf',
'vscvWWWvGWGGscbFMpRWFwQTPzfLQwQwPfLbzSzzDL',
'GvGBWpqcMVRNNZHgdHdtBJ',
'LchbZhjjZFjwSmPRqRffqbdtggdR',
'vWHMWlHJdGqtRqHV',
'MvzCJlnMnlTNnNNLLdhjjCdjjhDjjL',
'FNCllHFvCGvwQcPQJfgfmwgh',
'zjtRpbDLjtsrzbLLQmfBTgTBQQfhbfQB',
'WLgqRzqsrWvFGFZFZC',
'qjLlNcLjcNWpQLlQMmvmhCvCgsMZZghj',
'tGSDJtRGJzHMMGDVZCfvmfhzmZZgZsmv',
'BSSRDRHBGHtSSSbGJSwHbNcLQddqMNlrqcMQMldBWc',
'JSfctrtctDpszHvzVQHr',
'glCWjhWmFjlmlhmdWPhVVznvcHjszbvvpHvznv',
'FgBmFhCBCGFqglgmhCFmSTSRLJLLZfSRJcDSGMtM',
'vZGlFFtLMLdShSSShRVtVf',
'rQNvmznWPNCPNsrCsbWbsPCvjShhhfHBBHJjSJRhjSRnHhSj',
'mCNsQCmqszNcQzrzrrzWvGgGMgpdFpMLlFZGwcLDdg',
'QJRJQDlcqLlWbNGL',
'HCnwwsCrnstLWqtWNgZNgg',
'rsnTrTCHTnnVwnsVPqqDQcRjcczMPvPRzM',
'qCzjqnzVdzrdhnhddDbDBMPttcGBDBDPnc',
'sZgRQWHgWHHLsgsRRZsJbpJlDcDGNcTDFtGNFFcJNFPBPBTc',
'WggbRQSRRgRSsWWmbHqvVffVwhzvCdmfhmdV',
'lhqWcNpQGcNmmHmNPWCsQzQsgrQrBMCMbMVM',
'wDLFFDJvSFFZRDZSzCrzTzsRgVWbCrMW',
'dFwDtZfdjFZWFFfmHGPnPPmqfmPNcN',
'lcMRNJRGGLJnNVFbVrwrwZrD',
'tjCzQjQhQwgWFShVFS',
'ffHQsQssQTzBsPnLpMPRwsJP',
'MQSMSBSRFMQLJChLChjTBh',
'WmVlPrwnpwDlflNpDrNnDlDwThJCCdLJhhdhCfJTccGjvscd',
'gnDVnNnwgglwDwptSZFzgQHqbjZgZZ',
'nwBcFgwTDcNrpZMD',
'WQWCLZmvhMRvNjsNSD',
'CGGWmZGHHhtVzHbTqgTdbgzz',
'RmcTCwvssRbsThTcVRJJfSPqfJwJFqfjfMFq',
'zQNZDWtQlDZGBQPfFQqjJLjL',
'rrglggZGWnrnrrHlDhsbsPTVCsCVsTRpHv',
'wFGfzSvCPGttSzqwmtqmvvPRDDRCWgWWDTBTMcBcBWbCRM',
'hVJJHQHnpWnDTNnnDb',
'LJsVVdhQqvmdbbSf',
'srlJztzsVVsSsVtRlNllTWzzmqGhqWLPCDCgmChPLDdqCmCP',
'bZQMZpbvMBMgmDGmZLSPZd',
'MpScMSMpvfjMBcBcfMfSBnzlTjssNszrNrtlTVzlzFVN',
'rCtgrgClprGGClnJCZmwtMjZRjbjjcjZQv',
'PWVfBHWPdbNfbbRmRj',
'sPsVqFPsHWLhBVVqHFqPVddWSDLJgpTCnnrRRLGpJSSTRrgT',
'zjqpGjrQjGqSHCVvCrRZDN',
'cTdshMhdmcMNmddRHBhvCCBCCvHZDC',
'JTmTmJnLTdwzNQpPWJWgpP',
'BmpZmrzZnznHbpprSbQSQbqdSVqbPQcV',
'fRGTGJZRTTDwJTJRGDfgJgNFlSSFcldfdccFVlPlFFQPSQ',
'GvTTTZZLmsntzmCL',
'VhMcrmbhvzMSnhvftbRbllLtglBBtf',
'HqqqJqDqPjJPNjjDVFDZCdqBtRtGBGlGRfQQgttQfHlTQl',
'pCZJPqqZpmhvhpVh',
'dWLBJHJhGJGMBJRcDLDSQsSQpvcR',
'ZlnnPqglblfRRpSvSsnz',
'sPTgZVjjmwVTljrwTTlbwVGdJhBNNdFdMGNHHJMjBNFN',
'FhFrfbfgbLRdfqfrmvDgLdjrcQtSNStHHHQlSjJJPllt',
'CnspzZWTpCnMVzzZZGZRCzttHNjNlQlSNtNlNjVcjlQS',
'GCZsZBRwnvwfbqwFwb',
'bZnJFJgLFRnqQZqJQJFQGpCLNcGlLllClNtccjGc',
'rVfvwPDhPHGtlcbClr',
'mBhshsfMvBvqsQJdTbgnqQ',
'jgWHqMSWMGqWjWjqbWGJQDfVqLfrfDfJhVLfTr',
'pPplwsRZPFZFtLhfwgfwrhJL',
'zlRsdgFcRgmjdBCMHdjHWB',
'qJSGJSPQWzcprtQZtt',
'mBMVfsNBnZzcNtcc',
'LMLBsmMlvBgFsghVVvfgLBvbJJSqgGHqPGPtCWwbJHqCPG',
'ZvZLcdMGVMlHDvDpvqhH',
'NNSrQNbJbrTnnWZDDZqqhqpW',
'wbgNJrsrCwwJQZbsrJBFzjCCdzGdjcGzMdzj',
'JbVmdVLJJJdQMnzmmMgHjPqqjNgvqwngHNNP',
'ZfffDZZsRpcpRDcCRrlpplcWSSgwgSwjvvsjPSwhNSWggh',
'cCtfppZrpjtMMmdQQTLz',
'TtbnmbdmTmgTlPNhqvqj',
'wrwrLsVZRsJJJsfHjvPPWfhjHqRN',
'sDZwDvsCCQLJZQJQsMCMzZBtSMpndcSFnnSBFtSBmdBc',
'mWFTZdmQdZFrFQbCRsrspjSjnvCLRS',
'GwlDqcNHDzwGfHSRqCgJsSpnvpSL',
'NGlcNwHLLGfDDHDhDwDcwVczbPddZtMFWttWWtdPPdQdhPWd',
'mnfcZgcdZqnqdfFqPmHfhqsbgVMCJNMtvCJtMvtblTJtvb',
'rRLDDjPSjjPDGBQSBNbtLVtbMNNJlTMtbl',
'SzjDDzRRpGQDDDPHzdsmnnhsqcqdFq',
'ZDGNRDGjSdwnnmnsVNsHJJ',
'tMBWWrddLPLhvWTTPLccvmmbVpgsJHmccppJ',
'ClPrtBWWrhrFLBPlCRzjzGqdRzjRdRGZjF',
'csTRNQNJcNBDLfhfMf',
'qGmWpGHqrqPLChPRhVFPDD',
'tgHrtnrrJnZRTZcv',
'FLqrfmLDrqCmqjTqcbGqRTGVvb',
'FMtWMSWzzFStJzPzhWzhQvTvHVjjTjHTTHvbHc',
'PgtWWstWtSpZWPzWwnrBsdBDdFLfllLlfC',
'mThbMDMQDCDbwLqWpqPpdhwR',
'zgrcffgHNZltZSgHLsRsLLWRWgLqppsW',
'SVlSrfSHlSSVlrJfVctlNDMCmMFbnbRDbDBFJFbBRM',
'PrBrWqtRPdBLLrBwqpswgpwhgpnZhhzsgw',
'FTFRSVJQVJflFfQQgggGMZngGQZszZ',
'TbmfFJFSDFblSTDSFFbmVSDrPLLWtcmBqqRmBtmcLtcrjP',
'DjPsMwDjLVVTsvNNRTNTRT',
'ztdQQHqHlFNtfRNNNMgg',
'FzhMhHQlDcCrhCCc',
'zSHGzzmHgnnMDLTNTG',
'lPVBtvhQjpNSMWTLBD',
'VCftbjvbVCfPbZwsJsrSgSSZwC',
'CbwgmvMnmnCwMmwRQqJBGBgHZHpJHdtdZpJt',
'zVSlNSDlrzNhqlNTScDzVWfBBZZZZGBstGsdsWFpdHdJsW',
'NDlLzhrVcqRPCMRwLLLw',
'TjTHHLwnLjVlTwLjgVfvsFvDsdWfvDvFMd',
'qbRRRpmpcmDcczppztSqSvWFssFGfWdMvfQWdfsG',
'RZpqDBmtrzhzphjTgjHlnwjgJhgJ',
'dLmMgdgzwDLzDWFhBWvzFzzBZJ',
'tTVcppbSTfstTMMHfTbhBchhJFCWcjWBZhjGGB',
'SSSSNbsNRpRRsRrfVHfRpNtlPgQDLPdMmlDLlrPnqPdPLl',
'qqbTCSqdqqFZdRLZhwhZ',
'HWWlHtlrBfGtVssnsLnHfJVPPMMFzhPRwMPwFhzPZzPMGM',
'nfmtsrlsnrfVnHJrVBWlsVfgbbNTNSvmvvpcTjLjLbqvvS',
'GGhFvGPFcThqffPdnfNLqZZCSwtQSwZpwQQBsL',
'RglMRrJJgHBCBZSQQpdr',
'WmbRHHbzDgJMDzRDMdWmWHzHNFFvvGGhnvVvvfcvnFfcbvnT',
'QsfQmsLfZZZcshnJ',
'dSgdWgSVVFvzSpqFdqTgWRHbJNcbZNCTJCNNZRRCCh',
'FcpVjgDvVVFdVWFvzjwwQtBMLtBBGDwftPrB',
'rqsRrHsvsPqswNcJcNJrnnBrNn',
'bFjgGFdbVRNNnpRQpV',
'GSthhggGDSvMRqtHvMfM',
'ZwVPgMsgVsGzVsRZpgpzzgpFMrNbbLFrDLFFrrSDLfrNBN',
'qvnjBhQhntbfDLrF',
'CJlHHcHcTWqvpBdsWRpdPdgs',
'BjmTDjJBCBWrgQRPFlWWlW',
'dHphshtdtVHVhpJqspdvRrqFPgrLPPFPrrRPvQ',
'sdMsMtStVszpwMzHjJGjCcZjmScNfCDf',
'DmGdDffgDSDDdJstqdJldlRt',
'MhnvMCZCbbZHMvsCHtrcVrPjJcRqVtlt',
'LsQbsFZvZhQzZwhQWTNgBWpNwSGpTmfS',
'RRJQnCzbZZLTZJCBtWvFtsfqBqtfWb',
'prjlChGNldGNdlSVMhWfqWtfsvwvqsFtdtsq',
'GGjNDNhpMGMGVhrnZZTzcTHCCJcDHc',
'RmbMmjgpPjMBsBMfchhVsc',
'HwFWFTztSrtFpcQvBsSqVscBBC',
'zWwnJFHtWWHDgbGgdpGpnl',
'mnbWbRRLRFnmmWcCDTBVwCDBlwNW',
'ggJPtpdHGfdZtMHgtZgVPPBCVsPNBcsBTTDDCC',
'hpvJJTpGhdhtJdMHqvmmnLvSbmnFnRFm',
'WWtrWrNgVbRjMrQCNzqJFwQJFNTJ',
'LdHPhcdchQQssLzJrz',
'pBccnHpnrrcGHnnSlWjnRMSlbt',
'NMMfNFnZgMVThhTMcgTDJDJjsVvvJJqJmHsqHG',
'LQpwwprCQzBNBdGjGjHswswdvm',
'CBCzzCrbWbSlNQnTRgPPfFRWnfgc',
'RFwHVQRwFgTQSFVhdsdHsBdDBnnqnq',
'LGftLtPGGMzlNrhlPqPsrJ',
'fvGpWpMtccpTwwpRRQhh',
'TTJCGdTGtZRQQCnzcnCv',
'FWWHPSFNFbDbDDqSWnVmLRRjRRQLhcmLjS',
'qPwPWwFppbwggGZGfdJZgdnGdd',
'zSTWzrzWTLWpCtCGpqqGgplc',
'nZWwsJVZZBnJHJCclHllgtChgCgc',
'DFnVBJsFssVVFBFnBdfvjDSmTMWzrmMfRmTv',
'MJmgMssrsggqqMVstbwTcTbPbTTwThmw',
'NRBBGRjHVRRcRbCp',
'QnSfzLWzNHzNVQQVjrglJMsMFvgJdFWrgZ',
'ggLLGnhgnPvJHZnN',
'VBtmVSldbSBVlcNPHvjmNcwNZZ',
'tdWqSVSSBztVWGrThLhfrfvG',
'TDqrjdSwLqDppdTCdzPBFmmjQmhHFPFQhPFR',
'zlGbMcVcVtsPHFRhWRRsPF',
'btgvlVVcDZZZqgrz',
'DgwlgbbFDDjjPTHDrmddPhPV',
'WqtMBBtQsttMNWQBqsbJpGGzdPdTHLVmTzJhmTPhHHPTmH',
'qQsqGZNQtZGMNsNtZpFnjnCRbZffwwSRljFf',
'gMdFLCdnMZCTFFCqnTgWLCHfSgPgPHStcQQmfSBBSfHg',
'vrwwrwzbGjjswjvhGGsjPQmqRmHPbBtcBQtqfmcH',
'qzJllVsGVGljjsrzwDzhwzDGTddNLFnZWNdpCVWTNTZTLZCF',
'LtwMhDtctwbwwppdWBJQJBWPvPfDfqvG',
'FTzrNrgSRFrgzFRHNVFQJvlqHjBvQWlQWqPBfq',
'sFgNzmVmNzgTvVTMwhMhstMwZtsbsc',
'MrBDQVzzlrvhQzQrDMVQrzrzgRJnRRwwRbwSwwVRRNSgwwwJ',
'qFTPTvfTHcqqncpcwR',
'LmtdGGPmTPGCTLHLWsZMhvZMMMzrzzdlMQ',
'ZVNpjfpZNpfNgNjzNVfWtnbbWmBHtsZWBSZBGS',
'MrDrQvvDrPLDMvFvdmBGGsBBCtsHrnrGCm',
'ltRMwLLDDRlvQwvlQcwhqfcJNpgzjJpjhJ',
'sRRRlRbcFbBBdnFBwCGppNvGrTCDDGVNlr',
'PPSLQzHjzZZPLZPjgTNTgpCbVJvGrNCTGr',
'ZLHHPQjhQmWWSRRnssdtbnmfwF',
'GRwrMrHJGwJPGWsgfqQgsc',
'VbTvLQCZLSWWsgWf',
'TVDvVCvppvTDmzZVTbZpTzBBNQQQJlJBBJBNNJmRBwRH',
'shJRWJsjZGNjSTrjFS',
'dMLCddggldQzMCCVgzVVLmLvTwNFFSqpNSqSbFGSqTTpMTFN',
'VGQvVglCLcVzgdddCDVvlsPZRRBDJPHZWZZnBsWJRR',
'CrwlwhRCMrswnsHBFccHHWFc',
'QJTmtfQgLtzQfLQfdPcWSFHHDDSpcFpFBg',
'jTQTqbfQfmLbLQJbJrRCWjljZGjNrZlZlC',
'JmthDmLShtJmHphphJQCwjdjdFDzFgzFdgdNlC',
'sbMTVBrWMbNvVMnsWMnVzjsjwCfjFgfZzfdgdzlj',
'NvqbbBcMMPPSqLSpGGthmp',
'RfGWFHlPFFNWGFZRZBjvwCvzBwhhrvvjzmrr',
'sLJSLMSTSJTbStJtMSqSqbpMrvmrzWdvhmjDCzzwrrpjdDDv',
'SbQqsqsWcZPcQGFG',
'BjqbMqMVBsfqGqFqGLmF',
'ZZQbQPddPcwbPnRQltdtQZdnmFNrvfhGrhrWWFNWWtmNFNNW',
'dJJQccnRPpcbQcMHsSgSMsDMTJSg',
'WWGBBvPflnWbBWhvhbPvNfnnVCFZmVRVZmVGMVwRLCCCGwVC',
'gjszgTMrgzgqCRRdmJRjJLVw',
'grzQHzqczMSzqSHcgQsqPvPlbNblpPhhPPbHvnhp',
'sJDDNWdnRLTTvqwSFPCmLCCrCq',
'thzplgfjglflFcbMclpppMfcwPqCZQCmqCwrzCqmQmHSqPqq',
'MhcpFBMBlhjbBTdnNJWvNvsvBd',
'czwwghnWWfcfgwfWthfrvVvrjdrdvDDVrbzrLF',
'RHPPMRpQPRMPPJRjJQsZsrrvvJBDDVDVdFqrBrFdBv',
'smjMsGZHRsHSmRQNGHPpSTwwttCflwngnChcCtWW',
'bprrrwrtLDtrWwrQjRDQDbPPVHVmmmmHNWlPlVNPZZlv',
'hqqhfnBCTfnnhzJwzsqzfPZZMCCVZVHHFvZMFvZmlC',
'TzhhdJTqJzcBdJJnzjtQrLdjwgLtpbgrLQ',
'qzQvzzgWSCqtqqGpddGc',
'jLrZNZhZrNRLHNffhrjNjNdtdZtGcPFwFwpbGwbVpdwC',
'nHnhrLNCCMHmhHBMhrzvgJvsWSWMWzzWzSlv',
'RzcbzdRFzbbzbzbFdZFTHMZPhVhVQMLrlrQPhLZlMM',
'BNGfBvsNttVmMhlMLm',
'BwGjpllswfjwpcFDWcWcbpdb',
'SjzpswrLSDjVSpwlmZJBTBdNJLvBNvHQZT',
'rCcCtbqgCfthggtbGGMqqghqZQvvQTBNJQHQZQTcZTJFZFFd',
'CggGMtqMfWbbGghPhhbCMtmsSppSspjpmWzjVSWlVrrm',
'PmWTPThTQWnLWQFl',
'VNcSVfMbtsddBQNnNpdl',
'sSjctwjVSzzccjgnTnDTHRDhqjRR',
'WfMWfCNCjWWHNTccMjRjfRcMbqSwfVwqwsfGGbssrJSrswVw',
'llLFQLlvlPFnhQBPBZQBqvBwzSzGGhShJVwShmsJbbmzSG',
'lnPqvQZBFFBnnpgplFvtvHDjTdcTjTMMjCRNCMWgRC',
'rprFNFFNjNLmMdgcqL',
'BvzCQQbBQgffsDbvVHMdbcVqmLVqlmqq',
'JvJCzBDJwnsRnQDszCBnnnQBrjZPjFpgZFTFZRpTrpZFGFtT',
'wBHQQZHVCcpwDgdZdMsZjvMZFn',
'GPSzlNlJLfzzzvsWdWLMmFWLMM',
'NfqGSfrTNzRTqJfRbptQHFQFrwrFHBHw',
'sNjVMVNVMzPzQgghcMsNzJtjSJtTFDTJtJnnDLjDnL',
'CHwrdCpvCrwrWdpZqcpFttJSFJTLLHLJfbnbfD',
'qrlZCwlqZrqqpWdlRqCRqdqcVNsVMzQzmNgNPBsRhVQVVzMs']

#part1
for x in range(len(sackArray)):
    itemCount.append(len(sackArray[x]))
    compartments.append([sackArray[x][:(itemCount[x]//2)],sackArray[x][(itemCount[x]//2):]])
    dupItems.append(compare(compartments[x][0],compartments[x][1]))
    pri.append(char_position(dupItems[x]))

print(sum(pri))

#part2
x=0
pri2 = []
dup2 = 0
while x < (len(sackArray)):
    dup2 = (compare3(sackArray[x],sackArray[x+1],sackArray[x+2]))
    pri2.append(char_position(dup2))
    x=x+3
print(sum(pri2))
