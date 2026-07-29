"""Small hand-rolled SVG chart helpers -- no external charting library or CDN dependency,
so the dashboard renders correctly even with no internet access on the LAN."""

from markupsafe import Markup


def bar_chart_svg(data, width=480, height=220, padding=40):
    """data: list of (label, value, color) tuples."""
    if not data:
        return None
    max_val = max(v for _, v, _ in data) or 1
    n = len(data)
    plot_w = width - padding * 2
    plot_h = height - padding * 2
    gap = plot_w / n
    bar_w = gap * 0.6

    parts = [f'<line x1="{padding}" y1="{height - padding}" x2="{width - padding}" y2="{height - padding}" '
             f'stroke="#363646" stroke-width="1" />']
    for i, (label, value, color) in enumerate(data):
        bar_h = (value / max_val) * plot_h if max_val else 0
        x = padding + i * gap + (gap - bar_w) / 2
        y = padding + plot_h - bar_h
        parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{bar_h:.1f}" '
                      f'fill="{color}" rx="3" />')
        parts.append(f'<text x="{x + bar_w / 2:.1f}" y="{y - 6:.1f}" font-size="12" fill="#e6e6ec" '
                      f'text-anchor="middle">{value}</text>')
        parts.append(f'<text x="{x + bar_w / 2:.1f}" y="{height - padding + 18:.1f}" font-size="11" '
                      f'fill="#c7c7d6" text-anchor="middle">{label}</text>')

    svg = (f'<svg viewBox="0 0 {width} {height}" width="100%" height="{height}" '
           f'xmlns="http://www.w3.org/2000/svg">{"".join(parts)}</svg>')
    return Markup(svg)


def line_chart_svg(points, width=600, height=220, padding=40):
    """points: list of (label, value) tuples, in x-axis order."""
    if not points:
        return None
    max_val = max(v for _, v in points) or 1
    n = len(points)
    plot_w = width - padding * 2
    plot_h = height - padding * 2
    step = plot_w / max(n - 1, 1)

    coords = []
    for i, (label, value) in enumerate(points):
        x = padding + i * step
        y = padding + plot_h - (value / max_val) * plot_h
        coords.append((x, y, label, value))

    path_d = "M " + " L ".join(f"{x:.1f},{y:.1f}" for x, y, _, _ in coords)
    area_d = path_d + f" L {coords[-1][0]:.1f},{height - padding} L {coords[0][0]:.1f},{height - padding} Z"
    circles = "".join(
        f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="#6c6cf0"><title>{label}: {value}</title></circle>'
        for x, y, label, value in coords
    )

    label_every = max(1, n // 7)   # avoid crowding when there are many days
    labels = "".join(
        f'<text x="{x:.1f}" y="{height - padding + 18:.1f}" font-size="10" fill="#c7c7d6" '
        f'text-anchor="middle">{label}</text>'
        for idx, (x, y, label, value) in enumerate(coords) if idx % label_every == 0
    )
    axis = (f'<line x1="{padding}" y1="{height - padding}" x2="{width - padding}" y2="{height - padding}" '
            f'stroke="#363646" stroke-width="1" />')

    svg = (f'<svg viewBox="0 0 {width} {height}" width="100%" height="{height}" '
           f'xmlns="http://www.w3.org/2000/svg">'
           f'<path d="{area_d}" fill="#6c6cf033" stroke="none" />'
           f'<path d="{path_d}" fill="none" stroke="#6c6cf0" stroke-width="2" />'
           f'{circles}{axis}{labels}</svg>')
    return Markup(svg)
