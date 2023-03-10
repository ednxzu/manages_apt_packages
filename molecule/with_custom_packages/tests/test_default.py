"""Role testing files using testinfra."""


def test_hosts_file(host):
    """Validate /etc/hosts file."""
    etc_hosts = host.file("/etc/hosts")
    assert etc_hosts.exists
    assert etc_hosts.user == "root"
    assert etc_hosts.group == "root"

def test_packages_is_installed(host):
    """Validate mariadb-server, apache2 and consul are installed"""
    apt_package_mariadb = host.package("mariadb-server")
    apt_package_apache2 = host.package("apache2")
    apt_package_consul = host.package("consul")
    assert apt_package_mariadb.is_installed
    assert apt_package_apache2.is_installed
    assert apt_package_consul.is_installed
    assert apt_package_consul.version == "1.13.1-1"
