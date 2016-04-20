#"coding[:=]\s*([-\w.]+)" 1. 可以是：或者==。2.\s * 空格出现0或无限次；3.-或者单词字符或者换行外任何字符； 4.分组5. + 一次或者无限次

#-*-coding=utf-8-*-

from    win32api import MessageBox

class single_direction_link:
        node_count=0
        nodevalues=[]
        #nodeheads[]="" #不想用内建的链表
    def modify_value(self, index, newvalue):
        try:
            self.node
        except:
            MessageBox("error occurs when modifying the value of node %d",index)
        return
        pass
    def del_node(self, index):
        try:
            self.node_count-=self.node_count
        except:
            pass

        pass
    def add_node(self,index,newvalue):
        pass
    def modify_index(self,old_index,new_index):
        pass
    def __init__(self):
        self.node_count=0;
        # init one node
        #value should be set to 0
        pass


if __name__== __main__:
    mylink=single_direction_link()
    mylink.add_node(2,12)
