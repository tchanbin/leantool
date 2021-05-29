from . import route_api
from flask import request, jsonify, current_app
from ..models import S1Data, S4Data
import json, requests
from management import db
from .. import config
from openpyxl import Workbook, load_workbook


# 微信端登录，用code换取openid并返回微信。
@route_api.route("/login", methods=["GET", "POST"])
def login():
    AppSecret = "392ae660b903c06f31cf838fd0a9f781",
    AppID = "wxb7babc153cc97cd2"
    resp = {"code": 200, "msg": "操作成功", "data": {}, "errno": 0, "errmsg": "登录失败"}
    req = json.loads(request.get_data())
    code = req["data"]["code"] if "code" in req["data"] else ""
    if not code or len(code) < 1:
        resp["code"] = -1
        resp["msg"] = "需要code"
    # Wechat_Login_URI = "https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code={2}&grant_type=authorization_code".format(
    #     AppID, AppSecret, code)
    Wechat_Login_URI = "https://api.weixin.qq.com/sns/jscode2session?appid=wxb7babc153cc97cd2&secret=392ae660b903c06f31cf838fd0a9f781&js_code={0}&grant_type=authorization_code".format(
        code)
    r = requests.get(Wechat_Login_URI)
    res = json.loads(r.text)
    resp["openid"] = res["openid"]

    return jsonify(resp)


# 冲压工序获取数据
@route_api.route("/s1chongya", methods=["GET", "POST"])
def s1chongya():
    resp = {"code": 200, "msg": "初始化", "data": {}, "errno": 0}
    req = json.loads(request.get_data())
    openid = req["openid"]
    s1data = S1Data.query.filter_by(openid=openid).first()
    if s1data:
        # for data in req["data"]:
        #     name=data["name"]
        #     s1data.name=data["value"]

        s1data.cy_cycleTime = int(req["data"][0]["value"])
        s1data.cy_SMEDTime = int(req["data"][1]["value"])
        s1data.cy_upTime = int(req["data"][2]["value"])
        s1data.cy_Operators = int(req["data"][3]["value"])
        s1data.cy_EPE = int(req["data"][4]["value"])
        s1data.cy_runningTime = int(req["data"][5]["value"])
        s1data.cy_Wip = int(req["data"][6]["value"])
        s1data.cy_valueTime = int(req["data"][7]["value"])
    else:
        s1data = S1Data(
            openid=req["openid"],
            cy_cycleTime=int(req["data"][0]["value"]),
            cy_SMEDTime=int(req["data"][1]["value"]),
            cy_upTime=int(req["data"][2]["value"]),
            cy_Operators=int(req["data"][3]["value"]),
            cy_EPE=int(req["data"][4]["value"]),
            cy_runningTime=int(req["data"][5]["value"]),
            cy_Wip=int(req["data"][6]["value"]),
            cy_valueTime=int(req["data"][7]["value"]),

        )
    db.session.add(s1data)
    try:
        db.session.commit()
        resp["msg"] = "数据提交成功"
    except:
        db.session.rollback()
        resp["msg"] = "数据提交失败"

    return jsonify(resp)


# 机加工工序获取数据
@route_api.route("/s1jiJiaGong", methods=["GET", "POST"])
def s1jiJiaGong():
    resp = {"code": 200, "msg": "初始化", "data": {}, "errno": 0}
    req = json.loads(request.get_data())
    openid = req["openid"]
    s1data = S1Data.query.filter_by(openid=openid).first()
    if s1data:
        # for data in req["data"]:
        #     name=data["name"]
        #     s1data.name=data["value"]
        s1data.jjg_cycleTime = int(req["data"][0]["value"])
        s1data.jjg_SMEDTime = int(req["data"][1]["value"])
        s1data.jjg_upTime = int(req["data"][2]["value"])
        s1data.jjg_Operators = int(req["data"][3]["value"])
        s1data.jjg_Banci = int(req["data"][4]["value"])
        s1data.jjg_runningTime = int(req["data"][5]["value"])
        s1data.jjg_WipLeft = int(req["data"][6]["value"])
        s1data.jjg_WipRight = int(req["data"][7]["value"])
        s1data.jjg_valueTime = int(req["data"][8]["value"])
    else:
        s1data = S1Data(
            openid=req["openid"],
            jjg_cycleTime=int(req["data"][0]["value"]),
            jjg_SMEDTime=int(req["data"][1]["value"]),
            jjg_upTime=int(req["data"][2]["value"]),
            jjg_Operators=int(req["data"][3]["value"]),
            jjg_Banci=int(req["data"][4]["value"]),
            jjg_runningTime=int(req["data"][5]["value"]),
            jjg_WipLeft=int(req["data"][6]["value"]),
            jjg_WipRight=int(req["data"][7]["value"]),
            jjg_valueTime=int(req["data"][8]["value"]),

        )
    db.session.add(s1data)
    try:
        db.session.commit()
        resp["msg"] = "数据提交成功"
    except:
        db.session.rollback()
        resp["msg"] = "数据提交失败"

    return jsonify(resp)


# 焊接工序获取数据
@route_api.route("/s1hanJie", methods=["GET", "POST"])
def s1hanJie():
    resp = {"code": 200, "msg": "初始化", "data": {}, "errno": 0}
    req = json.loads(request.get_data())
    openid = req["openid"]
    # s1data = S1Data.query.filter_by(openid=openid).first()
    s1data = S1Data.query.filter_by(openid="oZcf_4_i7wqNzFBdlTmyucm4XGYs").first()
    if s1data:
        # for data in req["data"]:
        #     name=data["name"]
        #     s1data.name=data["value"]
        s1data.hj_cycleTime = int(req["data"][0]["value"])
        s1data.hj_SMEDTime = int(req["data"][1]["value"])
        s1data.hj_upTime = int(req["data"][2]["value"])
        s1data.hj_Operators = int(req["data"][3]["value"])
        s1data.hj_Banci = int(req["data"][4]["value"])
        s1data.hj_runningTime = int(req["data"][5]["value"])
        s1data.hj_WipLeft = int(req["data"][6]["value"])
        s1data.hj_WipRight = int(req["data"][7]["value"])
        s1data.hj_valueTime = int(req["data"][8]["value"])
    else:
        s1data = S1Data(
            openid=req["openid"],
            hj_cycleTime=int(req["data"][0]["value"]),
            hj_SMEDTime=int(req["data"][1]["value"]),
            hj_upTime=int(req["data"][2]["value"]),
            hj_Operators=int(req["data"][3]["value"]),
            hj_Banci=int(req["data"][4]["value"]),
            hj_runningTime=int(req["data"][5]["value"]),
            hj_WipLeft=int(req["data"][6]["value"]),
            hj_WipRight=int(req["data"][7]["value"]),
            hj_valueTime=int(req["data"][8]["value"]),

        )
    db.session.add(s1data)
    try:
        db.session.commit()
        resp["msg"] = "数据提交成功"
    except:
        db.session.rollback()
        resp["msg"] = "数据提交失败"

    return jsonify(resp)


# 装配1工序获取数据
@route_api.route("/s1ZP1", methods=["GET", "POST"])
def s1ZP1():
    resp = {"code": 200, "msg": "初始化", "data": {}, "errno": 0}
    req = json.loads(request.get_data())
    openid = req["openid"]
    s1data = S1Data.query.filter_by(openid=openid).first()
    if s1data:
        # for data in req["data"]:
        #     name=data["name"]
        #     s1data.name=data["value"]
        s1data.zp1_cycleTime = int(req["data"][0]["value"])
        s1data.zp1_SMEDTime = int(req["data"][1]["value"])
        s1data.zp1_upTime = int(req["data"][2]["value"])
        s1data.zp1_Operators = int(req["data"][3]["value"])
        s1data.zp1_Banci = int(req["data"][4]["value"])
        s1data.zp1_runningTime = int(req["data"][5]["value"])
        s1data.zp1_WipLeft = int(req["data"][6]["value"])
        s1data.zp1_WipRight = int(req["data"][7]["value"])
        s1data.zp1_valueTime = int(req["data"][8]["value"])
    else:
        s1data = S1Data(
            openid=req["openid"],
            ZP1_cycleTime=int(req["data"][0]["value"]),
            ZP1_SMEDTime=int(req["data"][1]["value"]),
            ZP1_upTime=int(req["data"][2]["value"]),
            ZP1_Operators=int(req["data"][3]["value"]),
            ZP1_Banci=int(req["data"][4]["value"]),
            ZP1_runningTime=int(req["data"][5]["value"]),
            ZP1_WipLeft=int(req["data"][6]["value"]),
            ZP1_WipRight=int(req["data"][7]["value"]),
            ZP1_valueTime=int(req["data"][8]["value"]),

        )
    db.session.add(s1data)
    try:
        db.session.commit()
        resp["msg"] = "数据提交成功"
    except:
        db.session.rollback()
        resp["msg"] = "数据提交失败"

    return jsonify(resp)


# 装配2工序获取数据
@route_api.route("/s1ZP2", methods=["GET", "POST"])
def s1ZP2():
    resp = {"code": 200, "msg": "初始化", "data": {}, "errno": 0}
    req = json.loads(request.get_data())
    openid = req["openid"]
    s1data = S1Data.query.filter_by(openid=openid).first()
    if s1data:
        # for data in req["data"]:
        #     name=data["name"]
        #     s1data.name=data["value"]
        s1data.zp2_cycleTime = int(req["data"][0]["value"])
        s1data.zp2_SMEDTime = int(req["data"][1]["value"])
        s1data.zp2_upTime = int(req["data"][2]["value"])
        s1data.zp2_Operators = int(req["data"][3]["value"])
        s1data.zp2_Banci = int(req["data"][4]["value"])
        s1data.zp2_runningTime = int(req["data"][5]["value"])
        s1data.zp2_WipLeft = int(req["data"][6]["value"])
        s1data.zp2_WipRight = int(req["data"][7]["value"])
        s1data.zp2_valueTime = int(req["data"][8]["value"])
    else:
        s1data = S1Data(
            openid=req["openid"],
            ZP2_cycleTime=int(req["data"][0]["value"]),
            ZP2_SMEDTime=int(req["data"][1]["value"]),
            ZP2_upTime=int(req["data"][2]["value"]),
            ZP2_Operators=int(req["data"][3]["value"]),
            ZP2_Banci=int(req["data"][4]["value"]),
            ZP2_runningTime=int(req["data"][5]["value"]),
            ZP2_WipLeft=int(req["data"][6]["value"]),
            ZP2_WipRight=int(req["data"][7]["value"]),
            ZP2_valueTime=int(req["data"][8]["value"]),

        )
    db.session.add(s1data)
    try:
        db.session.commit()
        resp["msg"] = "数据提交成功"
    except:
        db.session.rollback()
        resp["msg"] = "数据提交失败"

    return jsonify(resp)


# 客户获取数据
@route_api.route("/s1keHu", methods=["GET", "POST"])
def s1keHu():
    resp = {"code": 200, "msg": "初始化", "data": {}, "errno": 0}
    req = json.loads(request.get_data())
    openid = req["openid"]
    s1data = S1Data.query.filter_by(openid=openid).first()
    if s1data:
        # for data in req["data"]:
        #     name=data["name"]
        #     s1data.name=data["value"]

        s1data.kh_totalMonth = int(req["data"][0]["value"])
        s1data.kh_totalLeft = int(req["data"][1]["value"])
        s1data.kh_totalRight = int(req["data"][2]["value"])
        s1data.kh_huoPan = int(req["data"][3]["value"])
        s1data.kh_banCi = int(req["data"][4]["value"])

    else:
        s1data = S1Data(
            openid=req["openid"],
            kh_totalMonth=int(req["data"][0]["value"]),
            kh_totalLeft=int(req["data"][1]["value"]),
            kh_totalRight=int(req["data"][2]["value"]),
            kh_huoPan=int(req["data"][3]["value"]),
            kh_banCi=int(req["data"][4]["value"]),
        )
    db.session.add(s1data)
    try:
        db.session.commit()
        resp["msg"] = "数据提交成功"
    except:
        db.session.rollback()
        resp["msg"] = "数据提交失败"

    return jsonify(resp)


# s1发运获取数据
@route_api.route("/s1faYun", methods=["GET", "POST"])
def s1faYun():
    resp = {"code": 200, "msg": "初始化", "data": {}, "errno": 0}
    req = json.loads(request.get_data())
    openid = req["openid"]
    s1data = S1Data.query.filter_by(openid=openid).first()
    if s1data:
        # for data in req["data"]:
        #     name=data["name"]
        #     s1data.name=data["value"]

        s1data.fy_WipLeft = int(req["data"][0]["value"])
        s1data.fy_WipRight = int(req["data"][1]["value"])


    else:
        s1data = S1Data(
            openid=req["openid"],
            fy_WipLeft=int(req["data"][0]["value"]),
            fy_WipRight=int(req["data"][1]["value"]),

        )
    db.session.add(s1data)
    try:
        db.session.commit()
        resp["msg"] = "数据提交成功"
    except:
        db.session.rollback()
        resp["msg"] = "数据提交失败"

    return jsonify(resp)


# 供应商数据
@route_api.route("/s1gongYingShang", methods=["GET", "POST"])
def s1gongYingShang():
    resp = {"code": 200, "msg": "初始化", "data": {}, "errno": 0}
    req = json.loads(request.get_data())
    openid = req["openid"]
    s1data = S1Data.query.filter_by(openid=openid).first()
    if s1data:
        # for data in req["data"]:
        #     name=data["name"]
        #     s1data.name=data["value"]

        s1data.gys_supplier = req["data"][0]["value"]
        s1data.gys_logisticsWeek = req["data"][1]["value"]
        s1data.gys_size = int(req["data"][2]["value"])

    else:
        s1data = S1Data(
            openid=req["openid"],
            gys_supplier=int(req["data"][0]["value"]),
            gys_logisticsWeek=int(req["data"][1]["value"]),
            gys_size=int(req["data"][2]["value"]),

        )
    db.session.add(s1data)
    try:
        db.session.commit()
        resp["msg"] = "数据提交成功"
    except:
        db.session.rollback()
        resp["msg"] = "数据提交失败"

    return jsonify(resp)


# 查询所有已经获取数据
@route_api.route("/s1dataPage", methods=["GET", "POST"])
def s1dataPage():
    resp = {"code": 200, "msg": "初始化", "data": {}, "errno": 0}
    req = json.loads(request.get_data())
    openid = req["openid"]
    s1data = S1Data.query.filter_by(openid=openid).first()
    if s1data:
        # for data in req["data"]:
        #     name=data["name"]
        #     s1data.name=data["value"]
        s1gongYingShang = [{"label": "供应商名称", "value": s1data.gys_supplier},
                           {"label": "每周几送货", "value": s1data.gys_logisticsWeek},
                           {"label": "卷材尺寸（英尺/卷）", "value": s1data.gys_size},
                           ]

        s1keHu = [{"label": "月度总需求（件）", "value": s1data.kh_totalMonth},
                  {"label": " —左侧（件）", "value": s1data.kh_totalLeft},
                  {"label": "—右侧（件）", "value": s1data.kh_totalRight},
                  {"label": "货盘（件）", "value": s1data.kh_huoPan},
                  {"label": "班次（个）", "value": s1data.kh_banCi}, ]

        s1chongYa = [{"label": "周期时间（秒）", "value": s1data.cy_cycleTime},
                     {"label": " 换模时间（秒）", "value": s1data.cy_SMEDTime},
                     {"label": "开机率（%）", "value": s1data.cy_upTime},
                     {"label": "作业人员（个）", "value": s1data.cy_Operators},
                     {"label": "生产批次间隔（周）", "value": s1data.cy_EPE},
                     {"label": "可用时间（秒）", "value": s1data.cy_runningTime},
                     {"label": "工序前在制：卷材（天）", "value": s1data.cy_Wip},
                     {"label": "工序增值时间（秒）", "value": s1data.cy_valueTime}, ]

        s1jiJiaGong = [{"label": "周期时间（秒）", "value": s1data.jjg_cycleTime},
                       {"label": " 换模时间（秒）", "value": s1data.jjg_SMEDTime},
                       {"label": "开机率（%）", "value": s1data.jjg_upTime},
                       {"label": "作业人员（个）", "value": s1data.jjg_Operators},
                       {"label": "班次（班/天）", "value": s1data.jjg_Banci},
                       {"label": "可用时间（秒）", "value": s1data.jjg_runningTime},
                       {"label": "工序前在制：左侧件（天）", "value": s1data.jjg_WipLeft},
                       {"label": "工序前在制：右侧件（天）", "value": s1data.jjg_WipRight},
                       {"label": "工序增值时间（秒）", "value": s1data.jjg_valueTime}, ]

        s1hanJie = [{"label": "周期时间（秒）", "value": s1data.hj_cycleTime},
                    {"label": " 换模时间（秒）", "value": s1data.hj_SMEDTime},
                    {"label": "开机率（%）", "value": s1data.hj_upTime},
                    {"label": "作业人员（个）", "value": s1data.hj_Operators},
                    {"label": "班次（班/天）", "value": s1data.hj_Banci},
                    {"label": "可用时间（秒）", "value": s1data.hj_runningTime},
                    {"label": "工序前在制：左侧件（天）", "value": s1data.hj_WipLeft},
                    {"label": "工序前在制：右侧件（天）", "value": s1data.hj_WipRight},
                    {"label": "工序增值时间（秒）", "value": s1data.hj_valueTime}, ]

        s1ZP1 = [{"label": "周期时间（秒）", "value": s1data.zp1_cycleTime},
                 {"label": " 换模时间（秒）", "value": s1data.zp1_SMEDTime},
                 {"label": "开机率（%）", "value": s1data.zp1_upTime},
                 {"label": "作业人员（个）", "value": s1data.zp1_Operators},
                 {"label": "班次（班/天）", "value": s1data.zp1_Banci},
                 {"label": "可用时间（秒）", "value": s1data.zp1_runningTime},
                 {"label": "工序前在制：左侧件（天）", "value": s1data.zp1_WipLeft},
                 {"label": "工序前在制：右侧件（天）", "value": s1data.zp1_WipRight},
                 {"label": "工序增值时间（秒）", "value": s1data.zp1_valueTime}, ]

        s1ZP2 = [{"label": "周期时间（秒）", "value": s1data.zp2_cycleTime},
                 {"label": " 换模时间（秒）", "value": s1data.zp2_SMEDTime},
                 {"label": "开机率（%）", "value": s1data.zp2_upTime},
                 {"label": "作业人员（个）", "value": s1data.zp2_Operators},
                 {"label": "班次（班/天）", "value": s1data.zp2_Banci},
                 {"label": "可用时间（秒）", "value": s1data.zp2_runningTime},
                 {"label": "工序前在制：左侧件（天）", "value": s1data.zp2_WipLeft},
                 {"label": "工序前在制：右侧件（天）", "value": s1data.zp2_WipRight},
                 {"label": "工序增值时间（秒）", "value": s1data.zp2_valueTime}, ]

        s1faYun = [{"label": "工序前在制：左侧件（件）", "value": s1data.fy_WipLeft},
                   {"label": " 工序前在制：右侧件（件）", "value": s1data.fy_WipRight},
                   ]

        fullData = {"s1gongYingShang": s1gongYingShang,
                    "s1keHu": s1keHu,
                    "s1chongya": s1chongYa,
                    "s1jiJiaGong": s1jiJiaGong,
                    "s1hanJie": s1hanJie,
                    "s1ZP1": s1ZP1,
                    "s1ZP2": s1ZP2,
                    "s1faYun": s1faYun}
        fullData["msg"] = "数据获取成功"
        fullData["code"] = 200

    else:
        fullData = {}
        fullData["msg"] = "数据获取为空"

    return jsonify(fullData)


# # 生成vsm excel并返回excel的地址。先暂时放弃
# @route_api.route("/getVSM", methods=["GET", "POST"])
# def getVSM():
#     resp = {"code": 200, "msg": "初始化", "data": {}, "errno": 0}
#     req = json.loads(request.get_data())
#     openid = req["openid"]
#     s1data = S1Data.query.filter_by(openid=openid).first()
#     os.system("copy management/excel/vsm.xlsx management/excel/2.xlsx ")
#     # wb=load_workbook("management/excel/vsm.xlsx")
#     # sheet=wb["sheet1"]
#     # sheet["A1"]="test"True
#     # wb.save("management/excel/2.xlsx")
#     data = xlrd.open_workbook("management/excel/vsm.xls",formatting_info=True)
#
#     workbook = copy(data)
#     workbook.save('management/excel/2.xls')
#
#     return jsonify(resp)


# 返回计算过的数据
@route_api.route("/s1dataAnalysis", methods=["GET", "POST"])
def s1dataAnalysis():
    resp = {"code": 200, "msg": "初始化", "data": {}, "errno": 0}
    req = json.loads(request.get_data())
    openid = req["openid"]
    s1data = S1Data.query.filter_by(openid=openid).first()
    if s1data:
        # for data in req["data"]:
        #     name=data["name"]
        #     s1data.name=data["value"]
        s1gongYingShang = [{"label": "供应商名称", "value": s1data.gys_supplier},
                           {"label": "每周几送货", "value": s1data.gys_logisticsWeek},
                           {"label": "卷材尺寸（英尺/卷）", "value": s1data.gys_size},
                           ]

        s1keHu = [{"label": "月度总需求（件）", "value": s1data.kh_totalMonth},
                  {"label": " —左侧（件）", "value": s1data.kh_totalLeft},
                  {"label": "—右侧（件）", "value": s1data.kh_totalRight},
                  {"label": "货盘（件）", "value": s1data.kh_huoPan},
                  {"label": "班次（个）", "value": s1data.kh_banCi}, ]

        s1chongYa = [{"label": "周期时间（秒）", "value": s1data.cy_cycleTime},
                     {"label": " 换模时间（秒）", "value": s1data.cy_SMEDTime},
                     {"label": "开机率（%）", "value": s1data.cy_upTime},
                     {"label": "作业人员（个）", "value": s1data.cy_Operators},
                     {"label": "生产批次间隔（周）", "value": s1data.cy_EPE},
                     {"label": "可用时间（秒）", "value": s1data.cy_runningTime},
                     {"label": "工序前在制：卷材（天）", "value": s1data.cy_Wip},
                     {"label": "工序增值时间（秒）", "value": s1data.cy_valueTime}, ]

        s1jiJiaGong = [{"label": "周期时间（秒）", "value": s1data.jjg_cycleTime},
                       {"label": " 换模时间（秒）", "value": s1data.jjg_SMEDTime},
                       {"label": "开机率（%）", "value": s1data.jjg_upTime},
                       {"label": "作业人员（个）", "value": s1data.jjg_Operators},
                       {"label": "班次（班/天）", "value": s1data.jjg_Banci},
                       {"label": "可用时间（秒）", "value": s1data.jjg_runningTime},
                       {"label": "工序前在制：左侧件（天）", "value": s1data.jjg_WipLeft},
                       {"label": "工序前在制：右侧件（天）", "value": s1data.jjg_WipRight},
                       {"label": "工序增值时间（秒）", "value": s1data.jjg_valueTime}, ]

        s1hanJie = [{"label": "周期时间（秒）", "value": s1data.hj_cycleTime},
                    {"label": " 换模时间（秒）", "value": s1data.hj_SMEDTime},
                    {"label": "开机率（%）", "value": s1data.hj_upTime},
                    {"label": "作业人员（个）", "value": s1data.hj_Operators},
                    {"label": "班次（班/天）", "value": s1data.hj_Banci},
                    {"label": "可用时间（秒）", "value": s1data.hj_runningTime},
                    {"label": "工序前在制：左侧件（天）", "value": s1data.hj_WipLeft},
                    {"label": "工序前在制：右侧件（天）", "value": s1data.hj_WipRight},
                    {"label": "工序增值时间（秒）", "value": s1data.hj_valueTime}, ]

        s1ZP1 = [{"label": "周期时间（秒）", "value": s1data.zp1_cycleTime},
                 {"label": " 换模时间（秒）", "value": s1data.zp1_SMEDTime},
                 {"label": "开机率（%）", "value": s1data.zp1_upTime},
                 {"label": "作业人员（个）", "value": s1data.zp1_Operators},
                 {"label": "班次（班/天）", "value": s1data.zp1_Banci},
                 {"label": "可用时间（秒）", "value": s1data.zp1_runningTime},
                 {"label": "工序前在制：左侧件（天）", "value": s1data.zp1_WipLeft},
                 {"label": "工序前在制：右侧件（天）", "value": s1data.zp1_WipRight},
                 {"label": "工序增值时间（秒）", "value": s1data.zp1_valueTime}, ]

        s1ZP2 = [{"label": "周期时间（秒）", "value": s1data.zp2_cycleTime},
                 {"label": " 换模时间（秒）", "value": s1data.zp2_SMEDTime},
                 {"label": "开机率（%）", "value": s1data.zp2_upTime},
                 {"label": "作业人员（个）", "value": s1data.zp2_Operators},
                 {"label": "班次（班/天）", "value": s1data.zp2_Banci},
                 {"label": "可用时间（秒）", "value": s1data.zp2_runningTime},
                 {"label": "工序前在制：左侧件（天）", "value": s1data.zp2_WipLeft},
                 {"label": "工序前在制：右侧件（天）", "value": s1data.zp2_WipRight},
                 {"label": "工序增值时间（秒）", "value": s1data.zp2_valueTime}, ]

        s1faYun = [{"label": "工序前在制：左侧件（件）", "value": s1data.fy_WipLeft},
                   {"label": " 工序前在制：右侧件（件）", "value": s1data.fy_WipRight},
                   ]

        fullData = {"s1gongYingShang": s1gongYingShang,
                    "s1keHu": s1keHu,
                    "s1chongya": s1chongYa,
                    "s1jiJiaGong": s1jiJiaGong,
                    "s1hanJie": s1hanJie,
                    "s1ZP1": s1ZP1,
                    "s1ZP2": s1ZP2,
                    "s1faYun": s1faYun}
        # 按照25天，每天工作16个小计算
        # 客户节拍
        keHuTT = round(25 * 16 * 3600 / s1data.kh_totalMonth, 2)
        # 交付周期
        productionTime = round(s1data.cy_Wip + (s1data.jjg_WipLeft + s1data.jjg_WipRight) / keHuTT + (
                s1data.hj_WipLeft + s1data.hj_WipRight) / keHuTT + (
                                       s1data.zp1_WipLeft + s1data.zp1_WipRight) / keHuTT + (
                                       s1data.zp2_WipLeft + s1data.zp2_WipRight) / keHuTT + (
                                       s1data.fy_WipLeft + s1data.fy_WipRight) / keHuTT, 2)
        # 增值时间
        valueTime = round(
            s1data.cy_valueTime + s1data.jjg_valueTime + s1data.hj_valueTime + s1data.zp1_valueTime + s1data.zp2_valueTime,
            2)
        # 增值比
        valueRate = round(valueTime / (productionTime * 16 * 3600 * 1000), 6)

        respData = [
            {"label": "客户节拍（秒）", "value": keHuTT},
            {"label": "交付周期（天）", "value": productionTime},
            {"label": "增值时间（秒）", "value": valueTime},
            {"label": "增值比（‰）", "value": valueRate}
        ]

        resp["respData"] = respData

    return jsonify(resp)


# 供应商数据
@route_api.route("/s4gongYingShang", methods=["GET", "POST"])
def s4gongYingShang():
    resp = {"code": 200, "msg": "初始化", "data": {}, "errno": 0}
    req = json.loads(request.get_data())
    openid = req["openid"]
    s4data = S4Data.query.filter_by(openid=openid).first()
    if s4data:
        # for data in req["data"]:
        #     name=data["name"]
        #     s1data.name=data["value"]

        s4data.gys_supplier = req["data"][0]["value"]
        s4data.gys_logisticsWeek = req["data"][1]["value"]
        s4data.gys_size = int(req["data"][2]["value"])

    else:
        s4data = S4Data(
            openid=req["openid"],
            gys_supplier=int(req["data"][0]["value"]),
            gys_logisticsWeek=int(req["data"][1]["value"]),
            gys_size=int(req["data"][2]["value"]),

        )
    db.session.add(s4data)
    try:
        db.session.commit()
        resp["msg"] = "数据提交成功"
    except:
        db.session.rollback()
        resp["msg"] = "数据提交失败"

    return jsonify(resp)


# s4客户获取数据
@route_api.route("/s4keHu", methods=["GET", "POST"])
def s4keHu():
    resp = {"code": 200, "msg": "初始化", "data": {}, "errno": 0}
    req = json.loads(request.get_data())
    openid = req["openid"]
    s4data = S4Data.query.filter_by(openid=openid).first()
    if s4data:
        # for data in req["data"]:
        #     name=data["name"]
        #     s1data.name=data["value"]

        s4data.kh_totalMonth = int(req["data"][0]["value"])
        s4data.kh_totalLeft = int(req["data"][1]["value"])
        s4data.kh_totalRight = int(req["data"][2]["value"])
        s4data.kh_huoPan = int(req["data"][3]["value"])
        s4data.kh_banCi = int(req["data"][4]["value"])

    else:
        s4data = S4Data(
            openid=req["openid"],
            kh_totalMonth=int(req["data"][0]["value"]),
            kh_totalLeft=int(req["data"][1]["value"]),
            kh_totalRight=int(req["data"][2]["value"]),
            kh_huoPan=int(req["data"][3]["value"]),
            kh_banCi=int(req["data"][4]["value"]),
        )
    db.session.add(s4data)
    try:
        db.session.commit()
        resp["msg"] = "数据提交成功"
    except:
        db.session.rollback()
        resp["msg"] = "数据提交失败"

    return jsonify(resp)


# s4冲压工序获取数据
@route_api.route("/s4chongya", methods=["GET", "POST"])
def s4chongya():
    resp = {"code": 200, "msg": "初始化", "data": {}, "errno": 0}
    req = json.loads(request.get_data())
    openid = req["openid"]
    s4data = S4Data.query.filter_by(openid=openid).first()
    if s4data:
        # for data in req["data"]:
        #     name=data["name"]
        #     s1data.name=data["value"]

        s4data.cy_cycleTime = int(req["data"][0]["value"])
        s4data.cy_SMEDTime = int(req["data"][1]["value"])
        s4data.cy_upTime = int(req["data"][2]["value"])
        s4data.cy_Operators = int(req["data"][3]["value"])
        s4data.cy_EPE = int(req["data"][4]["value"])
        s4data.cy_runningTime = int(req["data"][5]["value"])
        s4data.cy_Wip = int(req["data"][6]["value"])
        s4data.cy_valueTime = int(req["data"][7]["value"])
    else:
        s4data = S4Data(
            openid=req["openid"],
            cy_cycleTime=int(req["data"][0]["value"]),
            cy_SMEDTime=int(req["data"][1]["value"]),
            cy_upTime=int(req["data"][2]["value"]),
            cy_Operators=int(req["data"][3]["value"]),
            cy_EPE=int(req["data"][4]["value"]),
            cy_runningTime=int(req["data"][5]["value"]),
            cy_Wip=int(req["data"][6]["value"]),
            cy_valueTime=int(req["data"][7]["value"]),

        )
    db.session.add(s4data)
    try:
        db.session.commit()
        resp["msg"] = "数据提交成功"
    except:
        db.session.rollback()
        resp["msg"] = "数据提交失败"

    return jsonify(resp)


# s4冲压工序获取数据
@route_api.route("/s4liuShuiXian", methods=["GET", "POST"])
def s4liuShuiXian():
    resp = {"code": 200, "msg": "初始化", "data": {}, "errno": 0}
    req = json.loads(request.get_data())
    openid = req["openid"]
    s4data = S4Data.query.filter_by(openid=openid).first()
    if s4data:
        # for data in req["data"]:
        #     name=data["name"]
        #     s1data.name=data["value"]

        s4data.lsx_cycleTime = int(req["data"][0]["value"])
        s4data.lsx_SMEDTime = int(req["data"][1]["value"])
        s4data.lsx_upTime = int(req["data"][2]["value"])
        s4data.lsx_Operators = int(req["data"][3]["value"])
        s4data.lsx_Banci = int(req["data"][4]["value"])
        s4data.lsx_runningTime = int(req["data"][5]["value"])
        s4data.lsx_WipLeft = int(req["data"][6]["value"])
        s4data.lsx_WipRight = int(req["data"][7]["value"])
        s4data.lsx_valueTime = int(req["data"][8]["value"])
    else:
        s4data = S4Data(
            openid=req["openid"],
            lsx_cycleTime=int(req["data"][0]["value"]),
            lsx_SMEDTime=int(req["data"][1]["value"]),
            lsx_upTime=int(req["data"][2]["value"]),
            lsx_Operators=int(req["data"][3]["value"]),
            lsx_Banci=int(req["data"][4]["value"]),
            lsx_runningTime=int(req["data"][5]["value"]),
            lsx_WipLeft=int(req["data"][6]["value"]),
            lsx_WipRight=int(req["data"][7]["value"]),
            lsx_valueTime=int(req["data"][8]["value"]),

        )
    db.session.add(s4data)
    try:
        db.session.commit()
        resp["msg"] = "数据提交成功"
    except:
        db.session.rollback()
        resp["msg"] = "数据提交失败"

    return jsonify(resp)


# s4发运获取数据
@route_api.route("/s4faYun", methods=["GET", "POST"])
def s4faYun():
    resp = {"code": 200, "msg": "初始化", "data": {}, "errno": 0}
    req = json.loads(request.get_data())
    openid = req["openid"]
    s4data = S4Data.query.filter_by(openid=openid).first()
    if s4data:
        # for data in req["data"]:
        #     name=data["name"]
        #     s1data.name=data["value"]

        s4data.fy_WipLeft = int(req["data"][0]["value"])
        s4data.fy_WipRight = int(req["data"][1]["value"])


    else:
        s4data = S4Data(
            openid=req["openid"],
            fy_WipLeft=int(req["data"][0]["value"]),
            fy_WipRight=int(req["data"][1]["value"]),

        )
    db.session.add(s4data)
    try:
        db.session.commit()
        resp["msg"] = "数据提交成功"
    except:
        db.session.rollback()
        resp["msg"] = "数据提交失败"

    return jsonify(resp)


# 返回计算过的数据
@route_api.route("/s4dataAnalysis", methods=["GET", "POST"])
def s4dataAnalysis():
    resp = {"code": 200, "msg": "初始化", "data": {}, "errno": 0}
    req = json.loads(request.get_data())
    openid = req["openid"]
    s4data = S4Data.query.filter_by(openid=openid).first()
    if s4data:
        # 按照25天，每天工作16个小计算
        # 客户节拍
        keHuTT = round(25 * 16 * 3600 / s4data.kh_totalMonth, 2)
        # 交付周期
        productionTime = round(s4data.cy_Wip + (s4data.lsx_WipLeft + s4data.lsx_WipRight) / keHuTT + (
                s4data.fy_WipLeft + s4data.fy_WipRight) / keHuTT, 2)
        # 增值时间
        valueTime = round(s4data.cy_valueTime + s4data.lsx_valueTime, 2)
        # 增值比
        valueRate = round(valueTime / (productionTime * 16 * 3600 * 1000), 6)

        respData = [
            {"label": "客户节拍（秒）", "value": keHuTT},
            {"label": "交付周期（天）", "value": productionTime},
            {"label": "增值时间（秒）", "value": valueTime},
            {"label": "增值比（‰）", "value": valueRate}
        ]

        resp["respData"] = respData

    return jsonify(resp)


# 查询未来价值流图所有已经获取数据
@route_api.route("/s4dataPage", methods=["GET", "POST"])
def s4dataPage():
    resp = {"code": 200, "msg": "初始化", "data": {}, "errno": 0}
    req = json.loads(request.get_data())
    openid = req["openid"]
    s4data = S4Data.query.filter_by(openid=openid).first()
    if s4data:
        # for data in req["data"]:
        #     name=data["name"]
        #     s4data.name=data["value"]
        s4gongYingShang = [{"label": "供应商名称", "value": s4data.gys_supplier},
                           {"label": "每周几送货", "value": s4data.gys_logisticsWeek},
                           {"label": "卷材尺寸（英尺/卷）", "value": s4data.gys_size},
                           ]

        s4keHu = [{"label": "月度总需求（件）", "value": s4data.kh_totalMonth},
                  {"label": " —左侧（件）", "value": s4data.kh_totalLeft},
                  {"label": "—右侧（件）", "value": s4data.kh_totalRight},
                  {"label": "货盘（件）", "value": s4data.kh_huoPan},
                  {"label": "班次（个）", "value": s4data.kh_banCi}, ]

        s4chongYa = [{"label": "周期时间（秒）", "value": s4data.cy_cycleTime},
                     {"label": " 换模时间（秒）", "value": s4data.cy_SMEDTime},
                     {"label": "开机率（%）", "value": s4data.cy_upTime},
                     {"label": "作业人员（个）", "value": s4data.cy_Operators},
                     {"label": "生产批次间隔（周）", "value": s4data.cy_EPE},
                     {"label": "可用时间（秒）", "value": s4data.cy_runningTime},
                     {"label": "工序前在制：卷材（天）", "value": s4data.cy_Wip},
                     {"label": "工序增值时间（秒）", "value": s4data.cy_valueTime}, ]

        s4liuShuiXian = [{"label": "周期时间（秒）", "value": s4data.lsx_cycleTime},
                         {"label": " 换模时间（秒）", "value": s4data.lsx_SMEDTime},
                         {"label": "开机率（%）", "value": s4data.lsx_upTime},
                         {"label": "作业人员（个）", "value": s4data.lsx_Operators},
                         {"label": "班次（班/天）", "value": s4data.lsx_Banci},
                         {"label": "可用时间（秒）", "value": s4data.lsx_runningTime},
                         {"label": "工序前在制：左侧件（天）", "value": s4data.lsx_WipLeft},
                         {"label": "工序前在制：右侧件（天）", "value": s4data.lsx_WipRight},
                         {"label": "工序增值时间（秒）", "value": s4data.lsx_valueTime}, ]

        s4faYun = [{"label": "工序前在制：左侧件（件）", "value": s4data.fy_WipLeft},
                   {"label": " 工序前在制：右侧件（件）", "value": s4data.fy_WipRight},
                   ]

        fullData = {"s4gongYingShang": s4gongYingShang,
                    "s4keHu": s4keHu,
                    "s4chongya": s4chongYa,
                    "s4liuShuiXian": s4liuShuiXian,
                    "s4faYun": s4faYun}
        fullData["msg"] = "数据获取成功"
        fullData["code"] = 200

    else:
        fullData = {}
        fullData["msg"] = "数据获取为空"

    return jsonify(fullData)
