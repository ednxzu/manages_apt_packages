"""Role testing files using testinfra."""


def test_hosts_file(host):
    """Validate /etc/hosts file."""
    etc_hosts = host.file("/etc/hosts")
    assert etc_hosts.exists
    assert etc_hosts.user == "root"
    assert etc_hosts.group == "root"

def test_packages_not_installed(host):
    """Validate nginx and apache2 are not installed"""
    apt_package_nginx = host.package("nginx")
    apt_package_apache2 = host.package("apache2")
    assert not apt_package_nginx.is_installed
    assert not apt_package_apache2.is_installed
