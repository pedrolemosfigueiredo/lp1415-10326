# -*- coding: utf-8 -*-
import xlrd
import sqlalchemy
book = xlrd.open_workbook("IPC_Portugal_1977_2013.xls")
engine = sqlalchemy.create_engine("sqlite:///ficheiro.db")
conn = engine.connect()
sheet1 = book.sheet_by_index(0)

conn.execute(
	"""
	create table if not exists IPC(
	Ano int, IPC_global double, variacao_anual double, 
	remun_min_mensal double, remun_max_mensal double,
	PIB_capita double, rend_bruto_per_capita double,
	rend_disponivel_per_capita double,
	remuneraçoes_per_capita double)
	"""
	)
for i in range(1, sheet1.nrows):
	conn.execute(
		"""
		insert into IPC values(?,?,?,?,?,?,?,?,?)
		""",sheet1.cell(i,1).value,sheet1.cell(i,2).value,
		sheet1.cell(i,3).value,sheet1.cell(i,4).value,
		sheet1.cell(i,5).value,sheet1.cell(i,6).value,
		sheet1.cell(i,7).value,sheet1.cell(i,8).value,
		sheet1.cell(i,9).value)