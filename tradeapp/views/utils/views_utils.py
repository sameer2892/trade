def get_dict(data):
    data1 = {}

    data1['futlink'] = data['futLink']
    data1['otherSeries'] = data['otherSeries']
    data1['lastUpdateTime'] = data['lastUpdateTime']
    data1['tradedDate'] = data['tradedDate']

    data_list = data['data'][0]
    data_list_new = []
    data_list_new.append({})
    data_list_new_item = data_list_new[0]

    data_list_new_item['extremeLossMargin'] = data_list['extremeLossMargin']
    data_list_new_item['cm_ffm'] = data_list['cm_ffm']
    data_list_new_item['bcStartDate'] = data_list['bcStartDate']
    data_list_new_item['change'] = data_list['change']
    data_list_new_item['buyQuantity3'] = data_list['buyQuantity3']
    data_list_new_item['sellPrice1'] = data_list['sellPrice1']
    data_list_new_item['buyQuantity4'] = data_list['buyQuantity4']
    data_list_new_item['sellPrice2'] = data_list['sellPrice2']
    data_list_new_item['priceBand'] = data_list['priceBand']
    data_list_new_item['buyQuantity1'] =  data_list['buyQuantity1']
    data_list_new_item['deliveryQuantity'] = data_list['deliveryQuantity']
    data_list_new_item['buyQuantity2'] = data_list['buyQuantity2']
    data_list_new_item['sellPrice5'] = data_list['sellPrice5']
    data_list_new_item['quantityTraded'] = data_list['quantityTraded']
    data_list_new_item['buyQuantity5'] = data_list['buyQuantity5']
    data_list_new_item['sellPrice3'] = data_list['sellPrice3']
    data_list_new_item['sellPrice4'] = data_list['sellPrice4']
    data_list_new_item['open'] = data_list['open']
    data_list_new_item['low52'] = data_list['low52']
    data_list_new_item['securityVar'] = data_list['securityVar']
    data_list_new_item['marketType'] = data_list['marketType']
    data_list_new_item['pricebandupper'] = data_list['pricebandupper']
    data_list_new_item['totalTradedValue'] = data_list['totalTradedValue']
    data_list_new_item['faceValue'] = data_list['faceValue']
    data_list_new_item['ndStartDate'] = data_list['ndStartDate']
    data_list_new_item['previousClose'] = data_list['previousClose']
    data_list_new_item['symbol'] = data_list['symbol']
    data_list_new_item['varMargin'] = data_list['varMargin']
    data_list_new_item['lastPrice'] = data_list['lastPrice']
    data_list_new_item['pChange'] = data_list['pChange']
    data_list_new_item['adhocMargin'] = data_list['adhocMargin']
    data_list_new_item['companyName'] = data_list['companyName']
    data_list_new_item['averagePrice'] = data_list['averagePrice']
    data_list_new_item['secDate'] = data_list['secDate']
    data_list_new_item['series'] = data_list['series']
    data_list_new_item['isinCode'] = data_list['isinCode']
    data_list_new_item['indexVar'] = data_list['indexVar']
    data_list_new_item['pricebandlower'] = data_list['pricebandlower']
    data_list_new_item['totalBuyQuantity'] = data_list['totalBuyQuantity']
    data_list_new_item['high52'] = data_list['high52']
    data_list_new_item['purpose'] = data_list['purpose']
    data_list_new_item['cm_adj_low_dt'] = data_list['cm_adj_low_dt']
    data_list_new_item['closePrice'] = data_list['closePrice']
    data_list_new_item['isExDateFlag'] = data_list['isExDateFlag']
    data_list_new_item['recordDate'] = data_list['recordDate']
    data_list_new_item['cm_adj_high_dt'] = data_list['cm_adj_high_dt']
    data_list_new_item['totalSellQuantity'] = data_list['totalSellQuantity']
    data_list_new_item['dayHigh'] = data_list['dayHigh']
    data_list_new_item['exDate'] = data_list['exDate']
    data_list_new_item['sellQuantity5'] = data_list['sellQuantity5']
    data_list_new_item['bcEndDate'] = data_list['bcEndDate']
    data_list_new_item['css_status_desc'] = data_list['css_status_desc']
    data_list_new_item['ndEndDate'] = data_list['ndEndDate']
    data_list_new_item['sellQuantity2'] = data_list['sellQuantity2']
    data_list_new_item['sellQuantity1'] = data_list['sellQuantity1']
    data_list_new_item['buyPrice1'] = data_list['buyPrice1']
    data_list_new_item['sellQuantity4'] = data_list['sellQuantity4']
    data_list_new_item['buyPrice2'] = data_list['buyPrice2']
    data_list_new_item['sellQuantity3'] = data_list['sellQuantity3']
    data_list_new_item['applicableMargin'] = data_list['applicableMargin']
    data_list_new_item['buyPrice4'] = data_list['buyPrice4']
    data_list_new_item['buyPrice3'] = data_list['buyPrice3']
    data_list_new_item['buyPrice5'] = data_list['buyPrice5']
    data_list_new_item['dayLow'] = data_list['dayLow']
    data_list_new_item['deliveryToTradedQuantity'] = data_list['deliveryToTradedQuantity']

    data1['data'] = data_list_new
    data1['optLink'] = data['optLink']

    return data1


def get_dict_for_loop(data):
    dict_new = {}
    for key, value in data.items():
        if key != "data":
            dict_new[key] = value
        else:
            data_list = []
            data_list.append({})
            for key_temp, value_temp in data[key][0].items():
                data_list[0][key_temp] = value_temp

            dict_new[key] = data_list

    return dict_new