
import newrelic.agent
newrelic.agent.initialize()
from aiohttp import web
import json
from subprocess import Popen

async def handle(request):
    response_obj = {'status': 'success'}
    newrelic.agent.record_custom_event('Execution',
                                       {'result': 'PASS', 'test_name': 'THIS WORKS', 'function_name': 'Handle'},
                                       newrelic.agent.application())
    Popen(['python3', 'test.py']) # Async bg process
    return web.Response(text=json.dumps(response_obj), status=200)

app = web.Application()
app.router.add_get('/', handle)


web.run_app(app)


