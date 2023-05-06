import json

from assertpy import assert_that

from client.http.eastblue_api import HttpEastBlueApi


class TestSeason:
    test_data={}
    def test_season_info(self):
        respon = HttpEastBlueApi().web_api_data_report_season()
        data = respon.get("data")
        assert_that(data, "data-report_season_data").is_not_empty()
        self.test_data["season_round"]=data.get("season_round")
        assert_that(data.get("season_round"), "data-report_season_data_season_round").is_not_empty()
        for i in data.get("season_round"):
            assert_that(i, "data-report_season_data_season_round_label").is_not_empty()
            assert_that(i, "data-report_season_data_season_round_value").is_not_empty()
        self.giftbag_list=data.get("giftbag_list")
        assert_that(self.giftbag_list, "data-report_season_data_giftbag_list").is_not_empty()
        for i in self.giftbag_list:
            assert_that(i, "data-report_season_data_giftbag_list_label").is_not_empty()
            assert_that(i, "data-report_season_data_giftbag_list_value").is_not_empty()

    def test_common_data_source(self):
        respon = HttpEastBlueApi().web_api_common_get_common_data_source(["mid"], "data-report")
        data = respon.get("data")
        assert_that(data, "data-report_season_data").is_not_empty()
        self.test_data["mid"]=data.get("mid")
        mid = data.get("mid")
        for i in mid:
            assert_that(i.get("label"), "data-report_season_data_mid_label").is_not_empty()
            assert_that(i.get("value"), "data-report_season_data_mid_value").is_not_nan()

    def test_season_basic_data_comparison_false(self):
        season_round_dict={}
        for i in self.test_data.get("season_round"):
            season_round_dict[i.get("label")]=i.get("value")
        respon = HttpEastBlueApi().web_api_data_report_season_basic_data(season_round_dict, ["2023-01-02 00:00:00","2023-04-05 23:59:59"])
        assert_that(respon.get("error_code"), "error_code").is_equal_to("0")

        data = respon.get("data")
        assert_that(data.get("second_query"), "data_second_query").is_none()
        if data.get("first_query") is not None:
            assert_that(len(data.get("first_query")), "data_second_query_length").is_less_than_or_equal_to(len(season_round_dict)+1)
            for i in data.get("first_query"):
                assert_that(i,"data_season_round").contains_key("season_round")
                assert_that(i.get("active_num"), "data_active_num").is_not_nan()
                assert_that(i.get("gt17_active_num"), "data_gt17_active_num").is_not_nan()
                assert_that(i.get("pay_dollar"), "data_pay_dollar").is_not_nan()
                assert_that(i.get("pay_num"), "data_pay_num").is_not_nan()
                assert_that(i.get("arppu"), "data_arppu").is_not_nan()
                assert_that(i.get("season_pay_dollar"), "data_season_pay_dollar").is_not_nan()
                assert_that(i.get("season_pay_num"), "data_season_pay_num").is_not_nan()
                assert_that(i.get("season_arppu"), "data_season_arppu").is_not_nan()
                assert_that(i.get("off_season_pay_dollar"), "data_off_season_pay_dollar").is_not_nan()
                assert_that(i.get("off_season_pay_num"), "data_off_season_pay_num").is_not_nan()
                assert_that(i.get("off_season_arppu"), "data_off_season_arppu").is_not_nan()
                assert_that(i.get("season_player_off_pay_dollar"), "data_season_player_off_pay_dollar").is_not_nan()
                assert_that(i.get("season_player_off_pay_share"), "data_season_player_off_pay_share").is_not_nan()
                assert_that(i.get("season_pay_share"), "data_season_pay_share").is_not_nan()
                assert_that(i.get("season_pay_num_share"), "data_season_pay_num_share").is_not_nan()
                assert_that(i.get("off_season_pay_share"), "data_off_season_pay_share").is_not_nan()
                assert_that(i.get("off_season_pay_num_share"), "data_off_season_pay_num_share").is_not_nan()

    def test_season_giftbag_group_comparison_false(self):
        season_round_dict={}
        for i in self.test_data.get("season_round"):
            season_round_dict[i.get("label")]=i.get("value")
        respon = HttpEastBlueApi().web_api_data_report_season_giftbag_group(season_round_dict, ["2023-01-02 00:00:00","2023-04-05 23:59:59"])
        assert_that(respon.get("error_code"), "error_code").is_equal_to("0")

        data = respon.get("data")
        assert_that(data.get("second_query"), "data_second_query").is_none()
        if data.get("first_query") is not None:
            for i in data.get("first_query"):
                assert_that(i,"data_season_round").contains_key("season_round","giftbag_id")
                assert_that(i.get("sale_dollar"), "data_sale_dollar").is_not_nan()
                assert_that(i.get("pay_num"), "data_pay_num").is_not_nan()



    def test_season_giftbag_level_comparison_false(self):
        season_round_dict={}
        for i in self.test_data.get("season_round"):
            season_round_dict[i.get("label")]=i.get("value")
        respon = HttpEastBlueApi().web_api_data_report_season_giftbag_level(season_round_dict, ["2023-01-02 00:00:00","2023-04-05 23:59:59"])
        assert_that(respon.get("error_code"), "error_code").is_equal_to("0")
        data = respon.get("data")
        assert_that(data.get("second_query"), "data_second_query").is_none()
        if data.get("first_query") is not None:
            for i in data.get("first_query"):
                assert_that(i,"data_season_round_pay_dollar_group").contains_key("season_round","pay_dollar_group")
                assert_that(i.get("sale_dollar"), "data_sale_dollar").is_not_nan()
                assert_that(i.get("pay_num"), "data_pay_num").is_not_nan()

    def test_season_source_score_comparison_false(self):
        season_round_dict={}
        for i in self.test_data.get("season_round"):
            season_round_dict[i.get("label")]=i.get("value")

        respon = HttpEastBlueApi().web_api_data_report_season_source_score(season_round_dict, ["2023-01-02 00:00:00","2023-04-05 23:59:59"],self.test_data.get("mid"))
        assert_that(respon.get("error_code"), "error_code").is_equal_to("0")
        data = respon.get("data")
        assert_that(data.get("second_query"), "data_second_query").is_none()
        if data.get("first_query") is not None:
            for i in data.get("first_query"):
                assert_that(i,"data_season_round_mid").contains_key("season_round","mid")
                assert_that(i.get("score"), "data_score").is_not_nan()
                assert_that(i.get("num"), "data_num").is_not_nan()
                assert_that(i.get("per_score"), "data_per_score").is_not_nan()

    #同时请求两个漏斗板块
    def test_season_source_funnel_comparison_false(self):
        season_round_dict={}
        for i in self.test_data.get("season_round"):
            season_round_dict[i.get("label")]=i.get("value")

        respon = HttpEastBlueApi().web_api_data_report_season_funnel(season_round_dict, ["2023-01-02 00:00:00","2023-04-05 23:59:59"])
        assert_that(respon.get("error_code"), "error_code").is_equal_to("0")
        data = respon.get("data")
        assert_that(data.get("first_query"), "data_first_query").is_not_empty()
        assert_that(data.get("second_query").get("gear"), "data_second_query_gear").is_none()
        assert_that(data.get("second_query").get("level"), "data_second_query_level").is_none()
        if data.get("first_query").get("gear") is not None:
            for i in data.get("first_query").get("gear"):
                assert_that(i,"data_season_round_mid").contains_key("season_round")
                assert_that(i.get("funnel_event"), "data_funnel_event").is_not_empty()
                assert_that(i.get("num"), "data_num").is_not_nan()

        if data.get("first_query").get("level") is not None:
            for i in data.get("first_query").get("level"):
                assert_that(i,"data_season_round_mid").contains_key("season_round","pay_dollar_group")
                assert_that(i.get("funnel_event"), "data_funnel_event").is_not_empty()
                assert_that(i.get("num"), "data_num").is_not_nan()

    # 请求分档位漏斗板块
    def test_season_source_funnel_gear_comparison_false(self):
        season_round_dict = {}
        for i in self.test_data.get("season_round"):
            season_round_dict[i.get("label")] = i.get("value")
        respon = HttpEastBlueApi().web_api_data_report_season_funnel(season_round_dict,["2023-01-02 00:00:00", "2023-04-05 23:59:59"],is_level_or_gear=False)
        assert_that(respon.get("error_code"), "error_code").is_equal_to("0")
        data = respon.get("data")
        assert_that(data.get("first_query"), "data_first_query").is_not_empty()
        assert_that(data.get("first_query").get("level"), "data_second_query_level").is_none()
        assert_that(data.get("second_query").get("gear"), "data_second_query_gear").is_none()
        assert_that(data.get("second_query").get("level"), "data_second_query_level").is_none()
        if data.get("first_query").get("gear") is not None:
            for i in data.get("first_query").get("gear"):
                assert_that(i, "data_season_round_mid").contains_key("season_round")
                assert_that(i.get("funnel_event"), "data_funnel_event").is_not_empty()
                assert_that(i.get("num"), "data_num").is_not_nan()

    #请求分层达成漏斗板块
    def test_season_source_funnel_level_comparison_false(self):
        season_round_dict = {}
        for i in self.test_data.get("season_round"):
            season_round_dict[i.get("label")] = i.get("value")
        respon = HttpEastBlueApi().web_api_data_report_season_funnel(season_round_dict,["2023-01-02 00:00:00", "2023-04-05 23:59:59"],is_level_or_gear=True)
        assert_that(respon.get("error_code"), "error_code").is_equal_to("0")
        data = respon.get("data")
        assert_that(data.get("first_query"), "data_first_query").is_not_empty()
        assert_that(data.get("first_query").get("gear"), "data_second_query_gear").is_none()
        assert_that(data.get("second_query").get("gear"), "data_second_query_gear").is_none()
        assert_that(data.get("second_query").get("level"), "data_second_query_level").is_none()
        if data.get("first_query").get("level") is not None:
            for i in data.get("first_query").get("level"):
                assert_that(i, "data_season_round_mid").contains_key("season_round", "pay_dollar_group")
                assert_that(i.get("funnel_event"), "data_funnel_event").is_not_empty()
                assert_that(i.get("num"), "data_num").is_not_nan()