#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import json
import re


def process_one_record(one_record: str):
    import re
    jsonstr = '{"台湾省":["台北市","新北市","桃园市","台中市","台南市","高雄市","基隆市","新竹市","嘉义市"],"澳门特别行政区":["花地玛堂区","圣安多尼堂区","大堂区","望德堂区","风顺堂区","嘉模堂区","圣方济各堂区"],"香港特别行政区":["九龙城区","北区","中西区","东区","南区","湾仔区","观塘区","深水埗区","黄大仙区","油尖旺区","离岛区","葵青区","西贡区","西贡区","沙田区","大埔区","荃湾区","屯门区","元朗区"],"北京市":["东城区","西城区","朝阳区","丰台区","石景山区","海淀区","门头沟区","房山区","通州区","顺义区","昌平区","大兴区","怀柔区","平谷区","密云区","延庆区"],"天津市":["和平区","河东区","河西区","南开区","河北区","红桥区","东丽区","西青区","津南区","北辰区","武清区","宝坻区","滨海新区","宁河区","静海区","蓟州区"],"河北省":["石家庄市","唐山市","秦皇岛市","邯郸市","邢台市","保定市","张家口市","承德市","沧州市","廊坊市","衡水市"],"山西省":["太原市","大同市","阳泉市","长治市","晋城市","朔州市","晋中市","运城市","忻州市","临汾市","吕梁市"],"内蒙古自治区":["呼和浩特市","包头市","乌海市","赤峰市","通辽市","鄂尔多斯市","呼伦贝尔市","巴彦淖尔市","乌兰察布市","兴安盟","锡林郭勒盟","阿拉善盟"],"辽宁省":["沈阳市","大连市","鞍山市","抚顺市","本溪市","丹东市","锦州市","营口市","阜新市","辽阳市","盘锦市","铁岭市","朝阳市","葫芦岛市"],"吉林省":["长春市","吉林市","四平市","辽源市","通化市","白山市","松原市","白城市","延边朝鲜族自治州"],"黑龙江省":["哈尔滨市","齐齐哈尔市","鸡西市","鹤岗市","双鸭山市","大庆市","伊春市","佳木斯市","七台河市","牡丹江市","黑河市","绥化市","大兴安岭地区"],"上海市":["黄浦区","徐汇区","长宁区","静安区","普陀区","虹口区","杨浦区","闵行区","宝山区","嘉定区","浦东新区","金山区","松江区","青浦区","奉贤区","崇明区"],"江苏省":["南京市","无锡市","徐州市","常州市","苏州市","南通市","连云港市","淮安市","盐城市","扬州市","镇江市","泰州市","宿迁市"],"浙江省":["杭州市","宁波市","温州市","嘉兴市","湖州市","绍兴市","金华市","衢州市","舟山市","台州市","丽水市"],"安徽省":["合肥市","芜湖市","蚌埠市","淮南市","马鞍山市","淮北市","铜陵市","安庆市","黄山市","滁州市","阜阳市","宿州市","六安市","亳州市","池州市","宣城市"],"福建省":["福州市","厦门市","莆田市","三明市","泉州市","漳州市","南平市","龙岩市","宁德市"],"江西省":["南昌市","景德镇市","萍乡市","九江市","新余市","鹰潭市","赣州市","吉安市","宜春市","抚州市","上饶市"],"山东省":["济南市","青岛市","淄博市","枣庄市","东营市","烟台市","潍坊市","济宁市","泰安市","威海市","日照市","莱芜市","临沂市","德州市","聊城市","滨州市","菏泽市"],"河南省":["郑州市","开封市","洛阳市","平顶山市","安阳市","鹤壁市","新乡市","焦作市","濮阳市","许昌市","漯河市","三门峡市","南阳市","商丘市","信阳市","周口市","驻马店市","济源市"],"湖北省":["武汉市","黄石市","十堰市","宜昌市","襄阳市","鄂州市","荆门市","孝感市","荆州市","黄冈市","咸宁市","随州市","恩施土家族苗族自治州","仙桃市","潜江市","天门市","神农架林区"],"湖南省":["长沙市","株洲市","湘潭市","衡阳市","邵阳市","岳阳市","常德市","张家界市","益阳市","郴州市","永州市","怀化市","娄底市","湘西土家族苗族自治州"],"广东省":["广州市","韶关市","深圳市","珠海市","汕头市","佛山市","江门市","湛江市","茂名市","肇庆市","惠州市","梅州市","汕尾市","河源市","阳江市","清远市","东莞市","中山市","潮州市","揭阳市","云浮市"],"广西壮族自治区":["南宁市","柳州市","桂林市","梧州市","北海市","防城港市","钦州市","贵港市","玉林市","百色市","贺州市","河池市","来宾市","崇左市"],"海南省":["海口市","三亚市","三沙市","儋州市","五指山市","琼海市","文昌市","万宁市","东方市","定安县","屯昌县","澄迈县","临高县","白沙黎族自治县","昌江黎族自治县","乐东黎族自治县","陵水黎族自治县","保亭黎族苗族自治县","琼中黎族苗族自治县"],"重庆市":["万州区","涪陵区","渝中区","大渡口区","江北区","沙坪坝区","九龙坡区","南岸区","北碚区","綦江区","大足区","渝北区","巴南区","黔江区","长寿区","江津区","合川区","永川区","南川区","璧山区","铜梁区","潼南区","荣昌区","开州区","梁平区","武隆区","城口县","丰都县","垫江县","忠县","云阳县","奉节县","巫山县","巫溪县","石柱土家族自治县","秀山土家族苗族自治县","酉阳土家族苗族自治县","彭水苗族土家族自治县"],"四川省":["成都市","自贡市","攀枝花市","泸州市","德阳市","绵阳市","广元市","遂宁市","内江市","乐山市","南充市","眉山市","宜宾市","广安市","达州市","雅安市","巴中市","资阳市","阿坝藏族羌族自治州","甘孜藏族自治州","凉山彝族自治州"],"贵州省":["贵阳市","六盘水市","遵义市","安顺市","毕节市","铜仁市","黔西南布依族苗族自治州","黔东南苗族侗族自治州","黔南布依族苗族自治州"],"云南省":["昆明市","曲靖市","玉溪市","保山市","昭通市","丽江市","普洱市","临沧市","楚雄彝族自治州","红河哈尼族彝族自治州","文山壮族苗族自治州","西双版纳傣族自治州","大理白族自治州","德宏傣族景颇族自治州","怒江傈僳族自治州","迪庆藏族自治州"],"西藏自治区":["拉萨市","日喀则市","昌都市","林芝市","山南市","那曲市","阿里地区"],"陕西省":["西安市","铜川市","宝鸡市","咸阳市","渭南市","延安市","汉中市","榆林市","安康市","商洛市"],"甘肃省":["兰州市","嘉峪关市","金昌市","白银市","天水市","武威市","张掖市","平凉市","酒泉市","庆阳市","定西市","陇南市","临夏回族自治州","甘南藏族自治州"],"青海省":["西宁市","海东市","海北藏族自治州","黄南藏族自治州","海南藏族自治州","果洛藏族自治州","玉树藏族自治州","海西蒙古族藏族自治州"],"宁夏回族自治区":["银川市","石嘴山市","吴忠市","固原市","中卫市"],"新疆维吾尔自治区":["乌鲁木齐市","克拉玛依市","吐鲁番市","哈密市","昌吉回族自治州","博尔塔拉蒙古自治州","巴音郭楞蒙古自治州","阿克苏地区","克孜勒苏柯尔克孜自治州","喀什地区","和田地区","伊犁哈萨克自治州","塔城地区","阿勒泰地区","石河子市","阿拉尔市","图木舒克市","五家渠市","铁门关市"]}'
    t = json.loads(jsonstr)
    def get_name_phone(s: str):
        name = s[0:s.index(',')]
        m = re.findall(r'1\d{10}',s)[0]

        # print(name, m)

        if not m:
            m = ""
        sub_s1 = s[s.index(',')+1:]
        phone_start = sub_s1.find(m)
        phone_end = phone_start +len(m)
        phone = sub_s1[phone_start:phone_end]
        sub_s2 = sub_s1[:phone_start] + sub_s1[phone_end:]
        #print(sub_s2)
        return name, phone, sub_s2

    def get_info_from_dict(s: str):
        for one_province in t.keys():
            if one_province.find(s) != -1:
                return one_province
        return s

    def get_shi(sheng:str, shi:str):
        for one_shi in t[sheng]:
            if one_shi.find(shi) != -1:
                return one_shi
        
        #print("not found shi,return null")
        return ""


    def get_address(address: str, lev: int):
        ##省，市，区(县），镇（街道），其他的
        #sheng = '',shi = '',qu_or_xian = '',zhen_or_jiedao = '',other = ''
        zhixianshi = ['北京市','上海市','重庆市','天津市']
        pos_sheng = address.find("省")
        if(pos_sheng != -1):
            sheng = address[:pos_sheng+1]
        else:
            sheng = get_info_from_dict(address[:2])
        
        # print(sheng)

        pos_sheng = 0
        i = 0
        if(sheng not in zhixianshi):
            
            while(i < len(sheng) and sheng[i]==address[i]):
                i += 1
        pos_sheng = i

        address = address[pos_sheng:]


        buchang_zizhizhou = 0
        pos_shi = address.find("自治州")
        if pos_shi != -1:
            buchang_zizhizhou = 2


        if pos_shi == -1:
            pos_shi = address.find("市")
            
    
        if pos_shi == -1:
            pos_shi = address.find("盟")
        
        


        if(pos_shi != -1):
            
            shi = address[:pos_shi + 1 + buchang_zizhizhou]
        else:
            shi = get_shi(sheng, address[:2])
        # print(shi)

        j = 0
        while(j < len(shi) and shi[j]==address[j]):
            j += 1

        address = address[j:]
        

        pos_qu = address.find("区")
        pos_xianjishi = address.find("市")
        pos_xian = address.find("县")
        pos_qi=address.find("旗")
        pos_dao=address.find("岛")    
        pos_quxian = -1

        if pos_quxian == -1:
            pos_quxian = pos_qu
        if pos_quxian == -1:
            pos_quxian = pos_xianjishi
        if pos_quxian == -1:
            pos_quxian = pos_qi       
        if pos_quxian == -1:
            pos_quxian = pos_dao
        if pos_quxian == -1:
            pos_quxian = pos_xian

        if pos_quxian != -1:
            quxian = address[:pos_quxian+1]
        else:
            quxian = ""
        # print(quxian)

        address = address[len(quxian):]
        # print(address)

        #镇，乡,街道
        pos_zj = address.find("镇")

        buchang = 0 #当为街道时，截取字符串需要加2
        if pos_zj == -1:
            pos_zj = address.find("街道")
            if pos_zj != -1:
                buchang = 1
        
        if pos_zj == -1 and buchang == 0:
            pos_zj = address.find("街")

        if pos_zj == -1 and buchang == 0:
            pos_zj =  address.find("乡")
      
        zhenjie = ""
        if pos_zj != -1:
            zhenjie = address[:pos_zj+ 1 + buchang]

        # print(zhenjie)

        other = address[len(zhenjie):]
        # print(zhenjie, " ", other)
        
        if sheng in zhixianshi:
            sheng = sheng[:-1]

        if lev == 1:
            res = [sheng, shi, quxian, zhenjie, other]
        elif lev >= 2:
            #处理路，门牌号，其他
            pos_lu = other.find("路")
            
            
            if pos_lu == -1:
                pos_lu = other.find("巷")
            
            if pos_lu == -1:
                pos_lu = other.find("村")
            
            lu = ""
            if pos_lu != -1:
                lu = other[:pos_lu+1]
                other = other[pos_lu+1:]

            hao = ""
            pos_menpaihao = other.find("号")
            if pos_menpaihao != -1:
                hao = other[:pos_menpaihao+1]
                other = other[pos_menpaihao+1:]
            
            res = [sheng, shi, quxian, zhenjie, lu, hao, other]
       
        return res
    level=0
    if one_record[:1]:
        level = int(one_record[:1])
    one_record = one_record[2:]
    name, phone, leftstr = get_name_phone(one_record)
    res = get_address(leftstr, level)
    temp = {
            "姓名":name,
            "手机":phone,
            "地址":res
        }
   
    return temp
    
ss=input()
if ss.endswith("."):
    ss = ss[:-1]
res=process_one_record(ss)
json1=json.dumps(res,ensure_ascii=False)
print(json1)


"""
"""  """
[{"answer":{"地址":["湖南省","长沙市","浏阳市","古港镇","024乡道古港镇梅田湖村村民委员会"],
"姓名":"宗衬缝","手机":"15590409121"},"input":"1!宗衬缝,湖南省长沙市浏阳市古港镇024乡道古港镇梅田15590409121湖村村民委员会."},
{"answer":{"地址":["北京","北京市","东城区","龙潭街道","夕阳寺大街16号院水上华城"],"姓名":"沈遵","手机":"15546305691"},
"input":"1!沈遵,北京市东城区龙潭街道夕阳寺大街16号院水15546305691上华城."}]

1!宗衬缝,湖南省长沙市浏阳市/；古港镇024乡道古港镇梅田15590409121湖村村民委员会.
1!沈遵,北京市东城区龙潭街道夕阳寺大街16号院水15546305691上华城.
"""
