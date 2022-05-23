#https://blog.amedama.jp/entry/2015/10/14/232045
import click

@click.command()
@click.option('--message', '-m', default='LGTM',
              show_default=True, help='画像に乗せる文字列')
@click.argument('keyword')
def cli():
    """LGTM画像作成ツール"""
    lgtm(keyword, message)
    click.echo('lgtm')

def lgtm():
    #ここにロジックを追加していく
    pass
