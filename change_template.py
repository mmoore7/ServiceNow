class Templates():
    master_files = [
        'CER - Rules',
        'ETX/ELT/HH1/HHS - SmartTools',
        'E0P - Action Criteria',
        'FLO - Flowsheets',
        'HFR - Registry',
        'HMT/HMP - Health Maintenance',
        'HRX - Report Info',
        'IDM - Dashboard Configurations',
        'IDB - Dashboard Component',
        'LPG/LRP - Print Group/Reports', #new
        'LVN - Navigator',
        'LQF - SmartForms', # new
        'PAF - Column',
        'VCG - Grouper',
    ]

    ebi_files = [
        'HRX - Report Info',
        'HGR/HGT/HGP/RPT - Report Templates',
        'HGT - Query Template',
        'IDM - Dashboard Configurations',
        'IDB - Dashboard Component',
        'RPT - Report Output Files',
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
        'E0P': {
            'title':'Update/Create Action Criteria Record',
            'ini': ['E0P'],
            'rsn': 'Action criteria record for Epic datalink.',
            'plan':'Create record or update existing one.\nWork with database admin to schedule datalink with this record.',
            'backout':'Remove datalink from the execution schedule in SQL server.',
            'test':'Run datalink in REL. Verify data was moved into Chronicles as expected.'
        },
        'HFR': {
            'title':'Update Registry',
            'ini':['HFR','VCG','CER'],
            'rsn':'Update registry rules and groupers',
            'plan':'Update the registry inclusion rule and/or metrics',
            'backout':'Undo the change',
            'test':"""Move to SUP.\nVerify configuration.\nProcess registry and/or metrics.\nVerify metric data is correct"""
        },
        'HGR': {
            'title':'Update Report Templates',
            'ini': ['HGR','HGT','HGP','RPT'],
            'rsn': 'Update Report Template',
            'plan': 'Update the template',
            'backout': 'Undo the change',
            'test':'Run report from template. Verify report runs as expected'
        },
        'HGT': {
            'title':'Update Query Template',
            'ini': ['HGT'],
            'rsn': 'Update Query Template',
            'plan': 'Update the template',
            'backout': 'Undo the change',
            'test':'Run report from template. Verify report runs as expected'
        },
        'HRX': {
            'title':'Update/Create Report Workbench Report',
            'ini': ['HRX','PAF'],
            'rsn': 'Update/Create Report',
            'plan': 'Create the report and/or update columns and report logic',
            'backout': 'Undo the change',
            'test': 'Run report. Verify it returns data as expected. Verify applicable columns sort as expected'
        },
        'HMT': {
            'title':'Update Existing Health Maintenance Topics/Plans',
            'ini':['HMT','HMP','CER'],
            'rsn':'Break/fix update',
            'plan':'Update the applicable HMT and/or HMP record.\nUpdate plan rule or registry completion metric.',
            'backout':'Undo changes',
            'test':'Open a patient chart.\nMake a change to the chart such as adding/removing an immunization.\nManually update health maintenance.\nVerify HMT appears as expected'
        },
        'IDM': {
            'title':'Update/Create Dashboard',
            'ini': ['IDM','IDB'],
            'rsn':'Dashboard configuration',
            'plan':'Build/update the dashboard',
            'backout':'Undo the changes',
            'test':'Open the dashboard. Verify dashboard displays data as expected. Verify dashboard reports run correctly.'
        },
        'IDB': {
            'title':'Update/Create Dashboard Component',
            'ini': ['IDB'],
            'rsn':'Dashboard component configuration',
            'plan':'Build/update the dashboard',
            'backout':'Undo the changes',
            'test':'Open the dashboard. Verify dashboard component displays data as expected. Verify dashboard reports run correctly.'
        },
        'LPG': {
            'title':'Change the Appearance or Order of a Hyperspace Display Report',
            'ini':['LPG','LRP'],
            'rsn':'Update and/or break/fix for hyperspace report/print group',
            'plan':'Update the print group and adjust layout/settings of report if applicable',
            'backout':'Undo the change',
            'test':'Open patient chart/encounter.\nVerify the report appears as expected'
        },
        'LVN': {
            'title':'Update or Add Navigators for Existing Care Management Navigator Templates (LVN, VCN)',
            'ini':['LVN','VCN'],
            'rsn':'New navigator section and/or break/fix for navigator',
            'plan':'Create the navigator section or topic.\nAdd VCN record if applicable.\nAdd section/topic to template',
            'backout':'Undo the change',
            'test':'Open a patient encounter.\nVerify the navigator appears and behaves as expected.'
        },
        'LQF': {
            'title':'Physically rearranging items, adding new button choices, or new text boxes on a SmartForm ',
            'ini':['LQF','HLX','E2X'],
            'rsn':'Update to existing smartform',
            'plan':'Update the smartform',
            'backout':'Undo the changes. If changes are large, create a new copy of smartform and move up. Revert to old smartform',
            'test':'Open patient encounter.\nVerify the smartform appears and behaves as expected.\nVerify smartdata elements file data as expected.'
        },
        'PAF': {
            'title':'Update/Create PAF Column',
            'ini':['PAF','LPP'],
            'rsn':'Update or create report workbench column',
            'plan':'Create column if applicable.\nUpdate column or associated LPP extension',
            'backout':'Undo the change',
            'test':'Add column to report.\nRun report and verify data appears as expected\nVerify sorting on column if applicable'
        },
        'RPT': {
            'title':'Update/Create Report Template Configuration',
            'ini': ['RPT'],
            'rsn': 'Configure templates for reporting',
            'plan': 'Make applicable changes to template',
            'backout': 'Undo the changes',
            'test': 'Run report from template. Verify it returns data as expected'
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
