#coding:utf-8

"""data manage"""


class DataManage(object):
    @staticmethod
    def manage_machine_list(result):
        """对从mysql中取出的服务器信息格式化为dict"""
        dic_data = {}
        num = 1
        for line in result:
            tmp_one_dic = dict()
            tmp_two_dic = dict()
            tmp_three_dic = dict()
            tmp_one_dic["server_ip"] = line[0].replace('\n', '<br/>')
            tmp_one_dic["public_ip"] = line[1].replace('\n', '<br/>')
            tmp_one_dic["idc_name"] = line[2]
            tmp_one_dic["mem_size"] = line[3]
            tmp_one_dic["cpu_num"] = line[4]
            tmp_one_dic["disk_size"] = line[5]
            tmp_one_dic["server_rack"] = line[6]
            tmp_one_dic["sn"] = line[7]
            tmp_one_dic["server_type"] = line[8]
            tmp_one_dic["os"] = line[9]
            tmp_one_dic["project_name"] = line[10]
            tmp_one_dic["server_status"] = line[11]
            tmp_two_dic["contact_name"] = line[12]
            tmp_two_dic["contact_info"] = line[13]
            tmp_one_dic["contact"] = tmp_two_dic
            #tmp_three_dic["comment_name"] = line[14]
            #tmp_three_dic["comment_info"] = line[15]
            #tmp_three_dic["comment_date"] = line[16]
            #tmp_one_dic["comment"] = tmp_three_dic
            tmp_one_dic["comment"] = line[14]
            tmp_one_dic["machine_id"] = line[15]

            ###如果需要生成json串的话，需要把下面一行改为dic_data[str(num)] = tmp_one_dic即可
            dic_data[num] = tmp_one_dic
            num += 1
        return dic_data

    @staticmethod
    def manage_add_host_select(result):
        tmp_dict = {}
        status_list = []
        tmp_list = ["idc", "project", "contact"]
        for name in range(len(tmp_list)):
            tmp_one_dict = {}
            for line in result[name]:
                if line[1].strip() == '':
                    pass
                else:
                    tmp_one_dict[line[0]] = line[1]
            tmp_dict[tmp_list[name]] = tmp_one_dict
        for num in range(len(result[3])):
            if result[3][num][0].strip() == '':
                pass
            else:
                status_list.append(result[3][num][0])
        return tmp_dict, status_list

    @staticmethod
    def manage_host_distribute(result):
        tmp_dict = {}
        for line in result:
            tmp_dict[line[0]] = {line[1]: line[2]}
        return tmp_dict

    @staticmethod
    def manage_host_export(result):
        import xlwt
        from ops import settings
        files = xlwt.Workbook(encoding='utf-8')
        table = files.add_sheet('sheet 1', cell_overwrite_ok=True)
        style = xlwt.XFStyle()
        font = xlwt.Font()
        font.name = "Times New Roman"
        style.font = font
        col = 0
        for key in settings.HOST_LIST_EXPORT:
            table.write(0, col, key, style)
            if col == 0 or col == 1 or col == 13:
                table.col(col).width = 0x0d00 + 2000
            col += 1
        for identify in range(1, len(result)+1):
            num = 0
            for content_col in settings.ADD_HOST_LIST:
                if content_col == "server_contact":
                    table.write(identify, num, result[identify]["contact"]["contact_name"])
                else:
                    table.write(identify, num, result[identify][content_col])
                num += 1
        files.save('ops/download/machine.xls')

    @staticmethod
    def manage_room_list(result, result_count):
        dic_data = dict()
        dic_data_count = dict()
        for line in result:
            tmp_dict = dict()
            tmp_dict["room_name"] = line[1]
            tmp_dict["room_contact"] = line[2]
            tmp_dict["contact_phone"] = line[3]
            tmp_dict["room_comment"] = line[4]
            dic_data[line[0]] = tmp_dict
        for line_count in result_count:
            dic_data_count[line_count[0]] = line_count[1]
        return dic_data, dic_data_count

    @staticmethod
    def manage_project_list(result):
        dic_data = dict()
        num = 1
        for line in result:
            tmp_dic = dict()
            tmp_dic["project_id"] = line[0]
            tmp_dic["project_name"] = line[1]
            dic_data[num] = tmp_dic
            num += 1
        return dic_data

    @staticmethod
    def manage_contact_list(result):
        dic_data = dict()
        num = 1
        for line in result:
            tmp_dic = dict()
            tmp_dic["contact_id"] = line[0]
            tmp_dic["contact_name"] = line[1]
            tmp_dic["contact_info"] = line[2]
            dic_data[num] = tmp_dic
            num += 1
        return dic_data