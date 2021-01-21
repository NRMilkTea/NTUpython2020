import json
import sys
from qt import *
from tools import *
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == '__main__':
	# initialization

	file = "maindata.json"

	data = []
	with open(file) as file:
		data = json.load(file)
	maindata = MainData(data)

	app = QtWidgets.QApplication(sys.argv)

	MainWindow = QtWidgets.QDialog()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)

	ui.tag_filter.addItems(["ALL"] + list(maindata.tags))

	ui.change_sorting(maindata.blocks)
	if len(maindata.blocks) != 0: ui.select_block(maindata.blocks[0])

	ui.tag_filter.currentIndexChanged.connect(lambda: ui.change_sorting(maindata.blocks))
	ui.sort_by.currentIndexChanged.connect(lambda: ui.change_sorting(maindata.blocks))
	ui.completeness.currentIndexChanged.connect(lambda: ui.change_sorting(maindata.blocks))
	ui.save.clicked.connect(lambda: ui.save_block(maindata))
	ui.delete.clicked.connect(lambda: ui.delete_qm(maindata))
	ui.complete.clicked.connect(lambda: ui.complete_block(maindata))
	ui.add_a_new_event.clicked.connect(lambda: ui.create_new_empty_block(maindata))

	MainWindow.show()
	sys.exit(app.exec_())