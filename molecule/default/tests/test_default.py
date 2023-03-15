"""Role testing files using testinfra."""


def test_hosts_file(host):
    """Validate /etc/hosts file."""
    etc_hosts = host.file("/etc/hosts")
    assert etc_hosts.exists
    assert etc_hosts.user == "root"
    assert etc_hosts.group == "root"

def test_packages_not_installed(host):
    """Validate vim is installed"""
    apt_package_vim = host.package("vim")
    assert apt_package_vim.is_installed
