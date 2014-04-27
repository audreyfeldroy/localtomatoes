from . import BaseTestCase

from localtomatoes import localtomatoes


class TestLocaltomatoes(BaseTestCase):

    def test_something(self):
        self.assertEquals(
            'Hello World!',
            localtomatoes(),
        )
