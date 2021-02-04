import os
import namegenerator

from umovme.cli import main
from umovme.client import UmovmeCenter

from unittest import TestCase


class TestGet(TestCase):

    def setUp(self):
        self.client = UmovmeCenter(os.environ.get('UMOVME_TOKEN'))

    def test_agent(self):
        resource_list = self.client.agent.search()

        result = self.client.agent.add(
            {
                'active': True,
                'agentType': {
                    'id': 89478,
                },
                'login': namegenerator.gen(),
                'name': 'kmee4 informatica ltda',
                'password': 'd421d8cd98f00b204e9800998ecf8427e',
            }
        )

        resource_list = self.client.agent.search()
        pass

