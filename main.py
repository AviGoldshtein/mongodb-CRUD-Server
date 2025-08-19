import uvicorn

# if __name__ == "__main__":
#     uvicorn.run("app.app:app", host="0.0.0.0", port=8000)



from services.dal.dal import DataLoader

dal = DataLoader()

# res = dal.insert_soldier("20123148", "Avi", "Gerds", "0548857174", "turai")
# res = dal.update_soldier("20852148", field='first_name', value="AVI")
# res = dal.delete_soldier("20852148")
res = dal.get_all_soldiers()
print(res)