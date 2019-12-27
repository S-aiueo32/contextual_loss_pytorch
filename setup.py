from setuptools import setup, find_packages

setup(
    name='contextual_loss_pytorch',
    version='latest',
    description='Contextual Loss w/ PyTorch',
    packages=find_packages(exclude=('tests', 'doc')),
    author='So Uchida',
    author_email='s.aiueo32@gmail.com',
    install_requires=["torch", "torchvision"],
    url='https://github.com/S-aiueo32/contextual_loss_pytorch',
)
