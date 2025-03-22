from fastapi import FastAPI, HTTPException
from qpython import qconnection

app = FastAPI()

# Connect to kdb+
q = qconnection.QConnection(host='localhost', port=5000)
q.open()

@app.get("/users")
def get_users():
    try:
        users = q("select from users")
        return {"users": users}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/portfolios/{trader}")
def get_portfolios(trader: str):
    try:
        portfolios = q(f"select from portfolios where owner='{trader}'")
        return {"portfolios": portfolios}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/holdings/{portfolio_id}")
def get_holdings(portfolio_id: str):
    try:
        holdings = q(f"select from holdings where portfolio_id='{portfolio_id}'")
        return {"holdings": holdings}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/execute_procedure/{procedure_name}")
def execute_procedure(procedure_name: str):
    try:
        q(f"{procedure_name}[]")
        return {"message": f"Procedure {procedure_name} executed successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.on_event("shutdown")
def shutdown():
    q.close()
