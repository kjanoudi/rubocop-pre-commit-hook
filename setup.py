from setuptools import find_packages
from setuptools import setup


setup(
    name='pre_commit_hooks',
    description='rubocop-git pre commit hook.',
    url='https://github.com/kjanoudi/rubocop-pre-commit-hook',
    version='0.1',

    author='Kareem Janoudi',
    author_email='kjanoudi@gmail.com',

    packages=find_packages('.', exclude=('tests*', 'testing*')),

    entry_points={
        'console_scripts': [
            'check-rubocop-git = pre_commit_hooks.check-rubocop-git:check-rubocop-git',
        ],
    },
)
