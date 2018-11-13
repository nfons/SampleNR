import os
import newrelic.agent
newrelic.agent.initialize()
newrelic.agent.register_application()

license = os.environ['NEW_RELIC_LICENSE_KEY']

# even though license and everything else is captured, NR doesnt send custom event
if __name__ == '__main__':
    print(license)
    newrelic.agent.record_custom_event('Execution',
                                       {'result': 'PASS', 'test_name': 'THIS DOES NOT WORK', 'function_name': 'Handle'},
                                       newrelic.agent.application())
