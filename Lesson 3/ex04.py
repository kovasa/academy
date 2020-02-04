import xml.etree.ElementTree as ET


def get_ch(el_list, i=0):
    res_list = []
    for child in el_list:
        j = i + 1
        ch_list, j = get_ch(child, j) if len(child) else ([], j)
        res_list.append({'name': child.tag, 'children': ch_list})
    return res_list, j


def parse_xml(xml_str):
    tree = ET.ElementTree(ET.fromstring(xml_str))
    root = tree.getroot()
    ch_list, i = get_ch(root)
    return {'name': root.tag, 'children': ch_list}, i


def test_parse():
    print(parse_xml('<root>\
                        <element1>\
                            <element5 />\
                        </element1>\
                        <element2 />\
                        <element3>\
                            <element4 />\
                        </element3>\
                    </root>'))
    print(parse_xml('<root>\
                        <element1 />\
                        <element2 />\
                        <element3>\
                            <element4>\
                                <element5 />\
                            </element4>\
                        </element3>\
                    </root>'))


test_parse()
