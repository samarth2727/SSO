import testcontainers
from testcontainers.generic import GenericContainer
from robot.api.deco import keyword

class TestcontainersLibrary:

    def __init__(self):
        self.container = None

    @keyword
    def start_sso_container(self, image_name):
        """Start the SSO container."""
        self.container = GenericContainer(image_name)
        self.container.start()
        return self.container.get_container_host_ip(), self.container.get_exposed_port(80)  # Adjust port as necessary

    @keyword
    def stop_sso_container(self):
        """Stop the SSO container."""
        if self.container:
            self.container.stop()
            self.container = None
