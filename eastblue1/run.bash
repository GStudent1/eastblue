export environment='test'
export game_id=97
export attribute_langs='all,es'
export sys_lang='zh-CN'

pytest test_case/test_season_monitoring
allure generate allure_report/xml -o allure_report/html --clean
