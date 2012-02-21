from setuptools import setup, find_packages

_extra_mako = ["Mako >= 0.1.1"]
setup(
    name='tw2.qrcode',
    version='2.0.2',
    description='Client-side QR Code Widget',
    author='Greg Jurman',
    author_email='gdj2214@rit.edu',
    license='MIT',
    url='http://github.com/gregjurman/tw2.qrcode',
    install_requires=[
        "tw2.core>=2.0b2",
        "tw2.jquery",
        ],
    extras_require={
        'mako': _extra_mako,
        },
    packages=find_packages(exclude=['ez_setup', 'tests']),
    tests_require = [
        'nose',
        'BeautifulSoup',
        'Genshi',
        'mako',
        # formencode isn't actually needed, but is just here to patch up
        # tw2.forms,
        'formencode',
        'strainer',
        'WebTest'
    ],
    namespace_packages = ['tw2'],
    zip_safe=False,
    include_package_data=True,
    test_suite = 'nose.collector',
    entry_points="""
        [tw2.widgets]
        # Register your widgets so they can be listed in the WidgetBrowser
        widgets = tw2.qrcode
    """,
    keywords = [
        'toscawidgets.widgets',
        'qrcode',
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: ToscaWidgets',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Widget Sets',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
