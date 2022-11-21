import os
import xml.etree.ElementTree as ET
path = os.getcwd()
os.mkdir("test")
t_path = path + "/test"
os.chdir(t_path)
os.mkdir("testset1")
os.mkdir("testset2")

def xyz(a,b):
    TEST = ET.Element("TEST",name=b)
    ownar = ET.SubElement(TEST, "ownar").text = a
    tree = ET.ElementTree(TEST)
    tree.write(b + ".xml")



set1_path = t_path +"/testset1"
os.chdir(set1_path)
xyz("Ganesh","small_test1")


set2_path = t_path +"/testset2"
os.chdir(set2_path)
xyz("Mangesh","big_test2")