from distutils.core import setup

from pkg_resources import parse_requirements

setup(
    name='roam_to_git',
    packages=['roam_to_git'],
    version='0.1',
    license='MIT',
    description='Automatic RoamResearch backup to Git',
    author='Tyler',  # Type in your name
    author_email='tyler@sprinter.dev',  # Type in your E-Mail
    url='https://github.com/twd-0004/roam-to-git',
    download_url='https://github.com/twd-0004/roam-to-git/archive/v0.1.tar.gz',
    keywords=['ROAMRESEARCH', 'GIT', 'BACKUP'],
    install_requires=[str(requirement) for requirement in
                      parse_requirements(open("requirements.txt"))],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Wiki',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    entry_points={
        'console_scripts': ['roam-to-git=roam_to_git.__main__:main'],
    }
)
