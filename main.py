# -*- coding: utf-8 -*-

# 1. 定义产品数据 (你可以轻松扩展到 10 款)
scooters = [
    {
        "model": "NL-City Light",
        "top_speed": 25,
        "range": "40km",
        "battery": "36V 10Ah",
        "price": "€449",
        "image": "images/scooter1.jpg"
    },
    {
        "model": "NL-Speed Master",
        "top_speed": 45,
        "range": "75km",
        "battery": "48V 15Ah",
        "price": "€899",
        "image": "images/scooter2.jpg"
    },
    {
        "model": "NL-Urban Glide",
        "top_speed": 25,
        "range": "55km",
        "battery": "36V 13Ah",
        "price": "€599",
        "image": "images/scooter1.jpg"
    },
    {
        "model": "NL-Touring Pro",
        "top_speed": 45,
        "range": "100km",
        "battery": "52V 20Ah",
        "price": "€1199",
        "image": "images/scooter2.jpg"
    },
]

# 2. HTML 模板构建
html_content = """
<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <script src="https://cdn.tailwindcss.com"></script>
    <title>Scooter Showcase - Netherlands</title>
</head>
<body class="bg-gray-100 p-8">
    <header class="max-w-7xl mx-auto mb-12 bg-white rounded-2xl shadow-sm border border-gray-200 px-8 py-5 grid grid-cols-3 items-center">
        <img src="images/Logo.jpg" alt="Scooter Showcase Logo" class="h-16 object-contain justify-self-start">
        <h1 class="text-4xl font-bold text-gray-800 text-center">Product Catalog</h1>
        <div></div>
    </header>
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
"""

# 3. 用 Python 逻辑生成每一个产品卡片
for s in scooters:
    # 自动判断荷兰路权：时速超过 25km/h 的需要特别标注
    legal_tag = ""
    if s['top_speed'] > 25:
        legal_tag = '<span class="bg-red-100 text-red-700 text-xs px-2 py-1 rounded">Private Road Only</span>'
    else:
        legal_tag = '<span class="bg-green-100 text-green-700 text-xs px-2 py-1 rounded">Road Legal (NL)</span>'

    card = f"""
    <div class="bg-white rounded-2xl shadow-sm hover:shadow-xl transition p-6 border border-gray-200">
        <img src="{s['image']}" class="w-full h-64 object-contain mb-4">
        <div class="flex justify-between items-start mb-2">
            <h2 class="text-2xl font-bold">{s['model']}</h2>
            {legal_tag}
        </div>
        <div class="grid grid-cols-2 gap-4 mt-4 text-sm text-gray-600">
            <div class="bg-gray-50 p-3 rounded"><b>Speed:</b> {s['top_speed']} km/h</div>
            <div class="bg-gray-50 p-3 rounded"><b>Range:</b> {s['range']}</div>
            <div class="bg-gray-50 p-3 rounded"><b>Battery:</b> {s['battery']}</div>
            <div class="bg-gray-50 p-3 rounded text-blue-600 font-bold"><b>Price:</b> {s['price']}</div>
        </div>
    </div>
    """
    html_content += card

# 4. 闭合产品网格，添加联系表单，闭合 HTML 标签并保存
html_content += """
</div>

<div class="max-w-2xl mx-auto mt-16 bg-white rounded-2xl shadow-sm border border-gray-200 p-8">
    <h2 class="text-2xl font-bold mb-2">Contact the Owner</h2>
    <p class="text-gray-500 text-sm mb-6">Have a question or want to place an order? Send us a message.</p>
    <form action="https://formspree.io/f/xvzygejg" method="POST" onsubmit="handleSubmit(event)" class="space-y-4">
        <input type="hidden" name="_subject" value="New scooter inquiry from website">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Name</label>
                <input name="name" type="text" placeholder="Your name" required
                    class="w-full border border-gray-300 rounded-lg px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500">
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Email</label>
                <input name="email" type="email" placeholder="you@example.com" required
                    class="w-full border border-gray-300 rounded-lg px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500">
            </div>
        </div>
        <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Message</label>
            <textarea name="message" rows="4" placeholder="Write your message here..." required
                class="w-full border border-gray-300 rounded-lg px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"></textarea>
        </div>
        <button type="submit"
            class="w-full bg-blue-600 text-white py-3 rounded-lg font-semibold hover:bg-blue-700 transition">
            Send Message
        </button>
    </form>
    <p id="success-msg" class="hidden mt-4 text-green-600 text-sm font-medium text-center">
        Message sent! We'll get back to you soon.
    </p>
    <p id="error-msg" class="hidden mt-4 text-red-600 text-sm font-medium text-center">
        Something went wrong. Please try again or email us directly.
    </p>
</div>

<script>
async function handleSubmit(e) {
    e.preventDefault();
    const form = e.target;
    const successMsg = document.getElementById('success-msg');
    const errorMsg = document.getElementById('error-msg');
    successMsg.classList.add('hidden');
    errorMsg.classList.add('hidden');

    try {
        const response = await fetch(form.action, {
            method: 'POST',
            body: new FormData(form),
            headers: { 'Accept': 'application/json' }
        });
        if (response.ok) {
            successMsg.classList.remove('hidden');
            form.reset();
        } else {
            errorMsg.classList.remove('hidden');
        }
    } catch (err) {
        errorMsg.classList.remove('hidden');
    }
}
</script>

</body></html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Successfully generated index.html!")