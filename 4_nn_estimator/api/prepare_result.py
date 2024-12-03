def prepare_date_to_api(latests_data = [], predicts = []) :
    results = []
    
    for item in latests_data:
        item_closed = {}
        item_predicted = {}
        
        item_closed["data"] = item[0].strftime("%Y-%m-%d")
        item_predicted["data"] = item[0].strftime("%Y-%m-%d")
        
        item_closed["valor"] = round(item[1], 2)
        item_predicted["valor"] = round(item[2],2)
        
        item_closed["tipo"] = '1'
        item_predicted["tipo"] = '2'
        
        item_closed["descricao"] = f'{item[0].strftime("%Y-%m-%d")} : fechado em {round(item[1],2)}'
        item_predicted["descricao"] = f'{item[0].strftime("%Y-%m-%d")} : previsto em {round(item[2],2)}'
        
        results.append(item_predicted)
        results.append(item_closed)
    
    results.reverse()
    
    for item in predicts:
        item_predicted = {}
        
        item_predicted["data"] = item['date']
        item_predicted["valor"] = round(item['predicted_close'],2)
        item_predicted["tipo"] = '2'
        item_predicted["descricao"] = f"{item.get('date', None)} : previsto em {round(item.get('predicted_close', None),2)}"
        
        results.append(item_predicted)
    
    return results
        
