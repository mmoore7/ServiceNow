class Templates():
    master_files = [
        'CER - Rules',
        'ETX/ELT/HH1/HHS - SmartTools',
        'FLO - Flowsheets',
        'HFR - Registry',
        'HMT/HMP - Health Maintenance',
        'HRX - Report Info',
        'LVN - Navigator',
        'PAF - Column',
        'VCG - Grouper',
    ]

    ebi_files = [
        'HRX - Report Info',
        'HGR - Report Templates',
        'HGT - Query Template',
        'HGP - Parameter Prompts',
        'RPT - Report Output Files',
        'IDM - Dashboard Configurations',
        'IDB - Dashboard Component'
    ]

    template = {
        'CER': {
            'title':'Update/Create Rule',
            'ini':['CER'],
            'rsn':'Update criteria/logic of rule',
            'plan':'Update the rule',
            'backout':'Undo the change',
            'test':'Verify rule passes as expected',
        },
        'FLO': {
            'title':'Update/Create Flowsheet (FLO, FLT), configuration related to SDOH and Care Management Workflows',
            'ini':['FLO','FLT'],
            'rsn':'Update/create flowsheet configuration',
            'plan':'Create flowsheet row/group if applicable.\nRelease flowsheet rows.\nAdd flowsheets to template.',
            'backout':'Unrelease the flowsheet',
            'test':'Open a patient encounter.\nVerify flowsheets appear as expected.\nVerify flowsheets store data as expected.'
        },
        'ETX': {
            'title':'Update/Create SmartTexts, SmartLists, SmartPhrases, and SmartLinks related to Care Management Workflows',
            'ini':['ETX','ELT','HH1','HHS'],
            'rsn':'New/updating documentation tool for care management users',
            'plan':'Create record or create new contact for existing record.\nComplete changes.\nRelease the record(s)',
            'backout':'Unrelease the contact of the record.',
            'test':'Open a patient encounter.\nDocument a note with the smart tool.\nVerify tool behaves as expected.'
        },
        'HFR': {
            'title':'Update Registry',
            'ini':['HFR','VCG','CER'],
            'rsn':'Update registry rules and groupers',
            'plan':'Update the registry inclusion rule and/or metrics',
            'backout':'Undo the change',
            'test':"""Move to SUP.\nVerify configuration.\nProcess registry and/or metrics.\nVerify metric data is correct"""
        },
        'HMT': {
            'title':'Update Existing Health Maintenance Topics/Plans',
            'ini':['HMT','HMP','CER'],
            'rsn':'Break/fix update',
            'plan':'Update the applicable HMT and/or HMP record.\nUpdate plan rule or registry completion metric.',
            'backout':'Undo changes',
            'test':'Open a patient chart.\nMake a change to the chart such as adding/removing an immunization.\nManually update health maintenance.\nVerify HMT appears as expected'
        },
        'LVN': {
            'title':'Update or Add Navigators for Existing Care Management Navigator Templates (LVN, VCN)',
            'ini':['LVN','VCN'],
            'rsn':'New navigator section and/or break/fix for navigator',
            'plan':'Create the navigator section or topic.\nAdd VCN record if applicable.\nAdd section/topic to template',
            'backout':'Undo the change',
            'test':'Open a patient encounter.\nVerify the navigator appears and behaves as expected.'
        },
        'PAF': {
            'title':'Update/Create PAF Column',
            'ini':['PAF','LPP'],
            'rsn':'Update or create report workbench column',
            'plan':'Create column if applicable.\nUpdate column or associated LPP extension',
            'backout':'Undo the change',
            'test':'Add column to report.\nRun report and verify data appears as expected\nVerify sorting on column if applicable'
        },
        'VCG': {
            'title':'Update/Create Grouper',
            'ini':['VCG'],
            'rsn':'Add/remove records from grouper',
            'plan':'Update the grouper',
            'backout':'Undo the change',
            'test':'Verify grouper has correct records'
        },
    }
