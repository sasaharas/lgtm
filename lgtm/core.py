#https://blog.amedama.jp/entry/2015/10/14/232045
import click

@click.command()
def cli():
    """LGTM画像作成ツール"""
    lgtm()
    click.echo('lgtm')#動作確認用

def lgtm():
    #ここにロジックを追加していく
    pass
