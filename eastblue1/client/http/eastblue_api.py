from client.http import HTTPClient
from constant import game_id, attribute_langs, sys_lang


class HttpEastBlueApi(HTTPClient):
    def __init__(self):
        super().__init__()

    def web_api_data_report_season(self):
        return self.send_request(
            method='POST',
            path='/web-api/data-report/season',
            data={
                "game_id": game_id,
                "attribute_langs": attribute_langs,
                "sys_lang": sys_lang
            }
        )

    def web_api_common_get_common_data_source(self, data_source_list, app_uri):
        return self.send_request(
            method='POST',
            path='/web-api/common/get-common-data-source',
            data={
                "game_id": game_id,
                "attribute_langs": attribute_langs,
                "sys_lang": sys_lang,
                "data_source_list": data_source_list,
                "options": {"app_uri":app_uri}
            }

        )
    def web_api_data_report_season_basic_data(self, season_round, season_duration, filtered_langs=None, is_internal=False, comparison=None, comparison_season_round=None, comparison_season_duration=None):
        if filtered_langs is None:
            filtered_langs = ["all"]
        return self.send_request(
            method='POST',
            path='/web-api/data-report/season-basic-data',
            data={
                "game_id": game_id,
                "attribute_langs": attribute_langs,
                "sys_lang": sys_lang,
                "season_round": season_round,
                "season_duration":season_duration,
                "filtered_langs":filtered_langs,
                "is_internal":is_internal,
                "comparison" :comparison,
                "comparison_season_round":comparison_season_round,
                "comparison_season_duration" :comparison_season_duration
            }
        )

    def web_api_data_report_season_giftbag_group(self, season_round, season_duration, filtered_langs=None, is_internal=False, comparison=None, comparison_season_round=None, comparison_season_duration=None):
        if filtered_langs is None:
            filtered_langs = ["all"]
        return self.send_request(
            method='POST',
            path='/web-api/data-report/season-giftbag-group',
            data={
                "game_id": game_id,
                "attribute_langs": attribute_langs,
                "sys_lang": sys_lang,
                "season_round": season_round,
                "season_duration":season_duration,
                "filtered_langs":filtered_langs,
                "is_internal":is_internal,
                "comparison" :comparison,
                "comparison_season_round":comparison_season_round,
                "comparison_season_duration" :comparison_season_duration
            }

        )

    def web_api_data_report_season_giftbag_level(self, season_round, season_duration,filtered_langs=None,pay_dollar=None,is_internal=False, comparison=None, comparison_season_round=None, comparison_season_duration=None):
        if pay_dollar is None:
            pay_dollar=[0,1000,10000,100000,333000]
        if filtered_langs is None:
            filtered_langs = ["all"]
        return self.send_request(
            method='POST',
            path='/web-api/data-report/season-giftbag-level',
            data={
                "game_id": game_id,
                "pay_dollar":pay_dollar,
                "attribute_langs": attribute_langs,
                "sys_lang": sys_lang,
                "season_round": season_round,
                "season_duration":season_duration,
                "filtered_langs":filtered_langs,
                "is_internal":is_internal,
                "comparison" :comparison,
                "comparison_season_round":comparison_season_round,
                "comparison_season_duration" :comparison_season_duration
            }

        )

    def web_api_data_report_season_source_score(self, season_round, season_duration,mid,filtered_langs=None,filters=None,pay_dollar=None,is_internal=False, comparison=None, comparison_season_round=None, comparison_season_duration=None):
        if pay_dollar is None:
            pay_dollar=[0,1000,10000,100000,333000]
        if filtered_langs is None:
            filtered_langs = ["all"]
        return self.send_request(
            method='POST',
            path='/web-api/data-report/season-source-score',
            data={
                "game_id": game_id,
                "pay_dollar":pay_dollar,
                "attribute_langs": attribute_langs,
                "sys_lang": sys_lang,
                "season_round": season_round,
                "season_duration":season_duration,
                "filtered_langs":filtered_langs,
                "is_internal":is_internal,
                "comparison" :comparison,
                "filters":filters,
                "mid":mid,
                "comparison_season_round":comparison_season_round,
                "comparison_season_duration" :comparison_season_duration
            }

        )

    def web_api_data_report_season_funnel(self, season_round, season_duration,gear_season_score=None,is_level_or_gear=None,level_season_score=None,filtered_langs=None,filters=None,pay_dollar=None,is_internal=False, comparison=None, comparison_season_round=None, comparison_season_duration=None):
        if filtered_langs is None:
            filtered_langs = ["all"]
        if is_level_or_gear is None:
            gear_season_score=[5000,10000,15000,20000,30000,40000,50000,60000,70000,80000]
            level_season_score=[5000,10000,15000,20000,30000,40000,50000,60000,70000,80000]
            pay_dollar=[0,1000,10000,100000,333000]
        if is_level_or_gear:
            level_season_score = [5000, 10000, 15000, 20000, 30000, 40000, 50000, 60000, 70000, 80000]
            pay_dollar = [0, 1000, 10000, 100000, 333000]
        else:
            gear_season_score = [5000, 10000, 15000, 20000, 30000, 40000, 50000, 60000, 70000, 80000]
        return self.send_request(
            method='POST',
            path='/web-api/data-report/season-funnel',
            data={
                "game_id": game_id,
                "pay_dollar":pay_dollar,
                "attribute_langs": attribute_langs,
                "sys_lang": sys_lang,
                "season_round": season_round,
                "season_duration":season_duration,
                "filtered_langs":filtered_langs,
                "is_internal":is_internal,
                "comparison" :comparison,
                "filters":filters,
                "gear_season_score":gear_season_score,
                "level_season_score":level_season_score,
                "comparison_season_round":comparison_season_round,
                "comparison_season_duration" :comparison_season_duration
            }

        )
