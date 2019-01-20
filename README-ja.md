<!-- -*- coding: utf-8 -*- -->
<!-- ----*---------*---------*---------*---------*---------*---------*---- -->
# markdown_markup_emoji

Markdownドキュメント中の絵文字をマークアップするための [Python-Markup][]
拡張です。
`<span class="emoji">😃</span>`のようにマークアップされるので、
絵文字を大きく<span class="emoji" style="font-size:150%">😃</span>
表示することができます。

### インストール

pipでインストールします。

```
$ pip install markdown_markup_emoji
```

### 利用方法

[Python-Markdown][] の拡張として使用します。

```.python
import markdown

md = markdown.Markdown(extensions=["markdown_markup_emoji.markup_emoji"])
md.convert("markdown text")
```

または、[Pelican][] から、Markdown拡張として使用します。

```.python
# pelicanconf.py
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown_markup_emoji.markup_emoji': {},
    },
    'output_format': 'html5',
}
```

### スタイルを追加

`<span class="emoji">😃</span>`のようにマークアップされるので、
すこし大きいフォントで表示されるように、スタイルを追加します。

```.css
.emoji { font-size: 150%; }
```

### 注意事項

絵文字フォントを含んでいませんので、表示はOSに依存します。
例えば、Windows7では絵文字は白黒で表示されたり、表示されないことがあります。
iOSやAndroid間では、違う絵文字が表示されることがあります。

[絵文字の一覧][EmojiList] は、こちらを参照してください。

[Python-Markdown]: https://github.com/Python-Markdown/markdown "Python-Markdown"
[Pelican]: https://blog.getpelican.com/ "Pelican Static Site Generator"
[EmojiList]: https://unicode.org/emoji/charts/full-emoji-list.html "Full Emoji List"
