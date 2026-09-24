import re, sys, html as H, collections

def inline(s):
    s = H.escape(s, quote=False)
    # Code spans first, held out of every later rule: `__name__` and `a*b*c` must stay literal.
    codes = []
    def hold(m):
        codes.append(m.group(1)); return f'\x00{len(codes)-1}\x00'
    s = re.sub(r'`([^`]+)`', hold, s)
    s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', s)
    # Autolinks <https://…> (escaped to &lt;…&gt; above) and the few inline HTML tags the corpus writes by hand.
    s = re.sub(r'&lt;(https?://[^\s&]+)&gt;', r'<a href="\1">\1</a>', s)
    s = re.sub(r'&lt;(/?)(sub|sup)&gt;', r'<\1\2>', s)
    s = re.sub(r'&lt;br\s*/?&gt;', '<br/>', s)
    s = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<![\w_])__(?!\s)(.+?)(?<!\s)__(?![\w_])', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<em>\1</em>', s)
    s = re.sub(r'\x00(\d+)\x00', lambda m: f'<code>{codes[int(m.group(1))]}</code>', s)
    return s

def convert(md):
    out, i, lines = [], 0, md.split('\n')
    while i < len(lines):
        ln = lines[i]
        if not ln.strip():
            i += 1; continue
        if ln.lstrip().startswith('```'):
            i += 1; buf = []
            while i < len(lines) and not lines[i].lstrip().startswith('```'):
                buf.append(lines[i]); i += 1
            i += 1
            out.append('<pre>' + H.escape('\n'.join(buf), quote=False) + '</pre>'); continue
        if re.match(r'^\s*(---|\*\*\*|___)\s*$', ln):
            out.append('<hr/>'); i += 1; continue
        m = re.match(r'^(#{1,6})\s+(.*)$', ln)
        if m:
            lv = len(m.group(1)); out.append(f'<h{lv}>{inline(m.group(2).strip())}</h{lv}>'); i += 1; continue
        if ln.lstrip().startswith('|') and i+1 < len(lines) and re.match(r'^\s*\|[\s:|-]+\|\s*$', lines[i+1]):
            rows = []
            while i < len(lines) and lines[i].lstrip().startswith('|'):
                rows.append(lines[i]); i += 1
            cells = lambda r: [c.strip() for c in r.strip().strip('|').split('|')]
            out.append('<table><thead><tr>' + ''.join(f'<th>{inline(c)}</th>' for c in cells(rows[0])) + '</tr></thead><tbody>')
            for r in rows[2:]:
                out.append('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in cells(r)) + '</tr>')
            out.append('</tbody></table>'); continue
        if ln.startswith('>'):
            buf = []
            while i < len(lines) and (lines[i].startswith('>') or (buf and lines[i].strip() and not re.match(r'^(#{1,6}\s|>|\s*[-*+]\s|\s*\d+\.\s)', lines[i]))):
                buf.append(re.sub(r'^>\s?', '', lines[i])); i += 1
            out.append('<blockquote>' + convert('\n'.join(buf)) + '</blockquote>'); continue
        m = re.match(r'^(\s*)([-*+]|\d+\.)\s+(.*)$', ln)
        if m:
            ordered = bool(re.match(r'^\d+\.$', m.group(2)))
            tag = 'ol' if ordered else 'ul'
            # A numbered list broken by blank lines arrives here one item at a time; keep its own number,
            # or every item prints as "1." and in-text references ("filter #5") point at nothing.
            start = int(m.group(2)[:-1]) if ordered else 1
            items, cur = [], None
            while i < len(lines):
                mm = re.match(r'^(\s*)([-*+]|\d+\.)\s+(.*)$', lines[i])
                if mm:
                    if cur is not None: items.append(cur)
                    cur = mm.group(3); i += 1
                elif lines[i].strip() and cur is not None and not re.match(r'^(#{1,6}\s|>|\s*(---|\*\*\*)\s*$)', lines[i]):
                    cur += ' ' + lines[i].strip(); i += 1
                else: break
            if cur is not None: items.append(cur)
            open_tag = f'<ol start="{start}">' if ordered and start != 1 else f'<{tag}>'
            out.append(open_tag + ''.join(f'<li>{inline(x)}</li>' for x in items) + f'</{tag}>'); continue
        buf = []
        while i < len(lines) and lines[i].strip() and not re.match(r'^(#{1,6}\s|>|\s*[-*+]\s|\s*\d+\.\s|\s*(---|\*\*\*|___)\s*$|\|)', lines[i]):
            buf.append(lines[i].strip()); i += 1
        if buf: out.append('<p>' + inline(' '.join(buf)) + '</p>')
    return '\n'.join(out)

def words(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    s = H.unescape(s)
    s = re.sub(r'[`*_#>|\[\]()-]+', ' ', s)
    return collections.Counter(w for w in re.findall(r"[0-9A-Za-zÀ-ỹ'’]+", s.lower()))

if __name__ == '__main__':
    raw = open(sys.argv[1], encoding='utf-8').read()
    parts = raw.split('---')
    body = '---'.join(parts[2:]) if raw.startswith('---') and len(parts) > 2 else raw
    fm = parts[1] if raw.startswith('---') else ''
    htm = convert(body)
    # compare RENDERED text: a markdown link's URL is an href, not visible text
    vis = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', body)
    a, b = words(vis), words(htm)
    missing, extra = a - b, b - a
    print('WORD-MULTISET DIFF  missing-from-html:', sum(missing.values()), ' extra-in-html:', sum(extra.values()))
    if missing: print('  MISSING:', dict(list(missing.items())[:25]))
    if extra:   print('  EXTRA  :', dict(list(extra.items())[:25]))
    open(sys.argv[2], 'w', encoding='utf-8').write(htm)
    print('links:', htm.count('<a href'), ' headings:', len(re.findall(r'<h[1-6]>', htm)),
          ' paras:', htm.count('<p>'), ' lists:', htm.count('<li>'), ' bold:', htm.count('<strong>'),
          ' literal-** left:', htm.count('**'))
