from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm  # Ensure this is add
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Log the user in
            return redirect(reverse('home'))  # Redirect to a success page
        else:
            # Invalid credentials, add an error message
            return render(request, 'login.html', {'error': 'Invalid credentials', 'form': request.POST})

    else:
        return render(request, 'login.html', {'form': None})  # Render an empty form on GET request


job_data = [
    {'title': 'Web Developer',
     'skills': ['HTML', 'CSS', 'JavaScript', 'Django', 'PHP', 'React', 'Node.js', 'Git', 'TypeScript', 'Sass',
                'RESTful APIs', 'jQuery', 'GraphQL', 'Web Accessibility', 'SEO Optimization']},
    {'title': 'Data Scientist',
     'skills': ['Python', 'Machine Learning', 'SQL', 'Data Visualization', 'Statistics', 'Deep Learning', 'R',
                'Big Data', 'NLP', 'TensorFlow', 'Pandas', 'NumPy', 'Data Mining', 'Data Cleaning']},
    {'title': 'Graphic Designer',
     'skills': ['Photoshop', 'Illustrator', 'InDesign', 'Figma', 'UX/UI Design', 'Sketch', 'Branding', 'Typography',
                'Web Design', 'Color Theory', 'Print Design', 'Motion Graphics', 'Logo Design']},
    {'title': 'Mobile App Developer',
     'skills': ['Java', 'Swift', 'React Native', 'Flutter', 'Kotlin', 'Dart', 'iOS Development',
                'Android Development', 'API Integration', 'Firebase', 'SQLite', 'Mobile UI Design', 'Agile Development']},
    {'title': 'Cloud Engineer',
     'skills': ['AWS', 'Azure', 'Docker', 'Kubernetes', 'Terraform', 'Google Cloud', 'Cloud Security',
                'Serverless Architecture', 'Cloud Migration', 'Networking', 'Automation', 'Load Balancing']},
    {'title': 'Cybersecurity Analyst',
     'skills': ['Network Security', 'Penetration Testing', 'Firewalls', 'Risk Assessment', 'Incident Response',
                'Malware Analysis', 'Vulnerability Assessment', 'Security Information and Event Management (SIEM)',
                'Encryption', 'Threat Intelligence', 'Security Policies']},
    {'title': 'DevOps Engineer',
     'skills': ['CI/CD', 'Jenkins', 'Ansible', 'Git', 'Docker', 'Kubernetes', 'Monitoring Tools',
                'Infrastructure as Code', 'Configuration Management', 'Scripting', 'Cloud Platforms', 'Performance Tuning']},
    {'title': 'Project Manager',
     'skills': ['Agile', 'Scrum', 'Stakeholder Management', 'Risk Management', 'Jira', 'Time Management',
                'Resource Allocation', 'Project Planning', 'Budget Management', 'Change Management', 'Team Leadership']},
    {'title': 'Digital Marketing Specialist',
     'skills': ['SEO', 'Content Marketing', 'Social Media', 'Google Analytics', 'PPC', 'Email Marketing',
                'Brand Management', 'Market Research', 'Copywriting', 'Conversion Rate Optimization (CRO)', 'Affiliate Marketing']},
    {'title': 'Game Developer',
     'skills': ['Unity', 'C#', 'Unreal Engine', '3D Modeling', 'Animation', 'Game Design', 'Virtual Reality',
                'Multiplayer Networking', 'Game Physics', 'Gameplay Programming', 'Level Design', 'Sound Design']},
]


# Companies ready to hire with images
companies_ready_to_hire = {
    'Web Developer': [
        {'name': 'IBM', 'image': 'https://fabrikbrands.com/wp-content/uploads/IBM-Logo-History-6.png'},
        {'name': 'GOOGLE',
         'image': 'https://yt3.googleusercontent.com/viNp17XpEF-AwWwOZSj_TvgobO1CGmUUgcTtQoAG40YaYctYMoUqaRup0rTxxxfQvWw3MvhXesw=s900-c-k-c0x00ffffff-no-rj'},
        {'name': 'Tech Innovations', 'image': 'https://techinnovations.in/images/logo.jpg'},
        {'name': 'Web Solutions Inc.', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRTKZXsnFGB-o4idKBPkgFQrEVqTGWPhwqBFA&s'},
        {'name': 'Future Web Corp', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSTl0m5J68WYzf0j-sGV1T_vY67kglv2EtvDA&s'},
    ],
    'Data Scientist': [
        {'name': 'TECHNOVALLEY', 'image': 'https://www.technovalley.co.in/wp-content/uploads/2019/05/technovalley-new.png'},
        {'name': 'FLIPKART', 'image': 'https://yt3.googleusercontent.com/cT40lDWqE99Ch52R3ftuAExjmjF-yZiY5rUSv_0Q3NXhcqzmiax8ReXuS4Qe53Fizcaw4hEX=s900-c-k-c0x00ffffff-no-rj'},
        {'name': 'Data Insights', 'image': 'https://media.licdn.com/dms/image/v2/C510BAQGQu4xyOYJuGw/company-logo_200_200/company-logo_200_200/0/1631398909122/datainsights_di_logo?e=2147483647&v=beta&t=VH3w2Ud8k5Iq5euWN1r3jUj1jGZaM1rinvvKbCYaBwc'},
        {'name': 'AI Analytics', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIJlbivFltGCbvz-GMKqBCvZTjLTYgaXWbPg&s'},
        {'name': 'Big Data Group', 'image': 'https://static.tildacdn.com/tild3832-3330-4233-b437-373265666538/___.png'},
    ],
    'Graphic Designer': [
        {'name': 'Creative Studio', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOu2u7wMlONs2mILaKEstkbf9rqoLs_ezSBw&s'},
        {'name': 'Design Pros', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_XnCUqpIFgA5L-tyVFr_WNRFJ8cYS20K1_w&s'},
        {'name': 'Visual Impact', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQl4JJNiFxFR754yRHBNkFlp4Z5TZpJM5nKvg&s'},
        {'name': 'Branding Agency', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRkDu2HhdBho8lW6c140IE8udmpSjlEHR6lw&s'},
        {'name': 'Artworks Co.', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRmtXa_yTlHnCqtH1KxssvWaMKq9wkjEXeGmQ&s'},
    ],
    'Mobile App Developer': [
        {'name': 'App Factory', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTEfV8WI1YcjPvesoEBkes2miBHKVOgljI9QA&s'},
        {'name': 'Mobile Masters', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSAQXfEDm9RSZZKNR19Sbavnu_XcjR-Z5IkLA&s'},
        {'name': 'Next Gen Apps', 'image': 'https://www.mobiloitte.com/blog/wp-content/uploads/2023/08/Next-Gen-Mobile-Apps.jpg'},
        {'name': 'Smart Apps Inc.', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTmTDnKWohW1xyN5yGxkToU6T82AgSZA72v7A&s'},
        {'name': 'App Innovators', 'image': 'https://play-lh.googleusercontent.com/VeU4yM7nFse9RndssMMfHM-AYvfYCf8TKS1XFpc8RNA-OQE1lQ3xqOGPDxfCLZ5lRio=w526-h296-rw'},
    ],
    'Cloud Engineer': [
        {'name': 'Cloud Solutions', 'image': 'data:image/jpeg;base64,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'},
        {'name': 'Sky High Tech', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQgn0mszR5yYwuQRFCIJtMJ0ZM3qktEij2Ycg&s'},
        {'name': 'CloudWorks', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ6LsEfFJjQcCsJE5hlBOuvxo9d0EjmDvAyJg&s'},
        {'name': 'Nimbus Inc.', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTrkTW8IAAHKeJBpKxwODazYLLfrOMkebzPXA&s'},
        {'name': 'Cloudify', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGgZEc7Bx2AXck1REuj55qZHDuZJVjIoH0jQ&s'},
    ],
    'Cybersecurity Analyst': [
        {'name': 'SecureTech', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ6ef6f_YWJLSUaIufoAIfsaMX9iUCynuloXA&s'},
        {'name': 'CyberGuard', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwpBk33vg-wxGgwH8YzxC1ztkcbB4YXfyYUg&s'},
        {'name': 'SafeNet', 'image': 'https://www.cloudworks.no/hubfs/raw_assets/public/Cloudworks_October2021/images/cloudworks-logo.svg'},
        {'name': 'Fortify Inc.', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTldS4JlNK_Zdnv5Q3e7ZlaUvVA0aS1xzEa0w&s'},
        {'name': 'Shield Cybersecurity', 'image': 'https://content.presentermedia.com/files/clipart/00029000/29606/cybersecurity_sheild_800_wht.jpg'},
    ],
    'DevOps Engineer': [
        {'name': 'DevOps Solutions', 'image': 'url_to_devops_solutions.jpg'},
        {'name': 'AgileOps', 'image': 'url_to_agileops.jpg'},
        {'name': 'Ops Masters', 'image': 'url_to_ops_masters.jpg'},
        {'name': 'Continuous Tech', 'image': 'url_to_continuous_tech.jpg'},
        {'name': 'SysOps Corp', 'image': 'url_to_sysops.jpg'},
    ],
    'Project Manager': [
        {'name': 'ManageIt', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQsSPRUMRKZhnvsVYweepd2n3XHvpRbp-cPTA&s'},
        {'name': 'Project Pros', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhpw7o0geA1OHzd-VsvcqLQ-StjsS7W1T8ZQ&s'},
        {'name': 'Task Masters', 'image': 'https://m.media-amazon.com/images/M/MV5BY2RmNmM1YzAtOWJlMi00NTdiLWEwN2MtNDliNGI3NmUxMTk3XkEyXkFqcGc@._V1_.jpg'},
        {'name': 'Visionary Projects', 'image': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAe8AAABmCAMAAADVn+lbAAABVlBMVEX///9AIwhtsSI+IAA1EAA4FQA2EgDDurMrAAAwAQA0DQDk4N08HQBGJgCbj4YzCwBPNB6JfXU7GwChlIpCIgA5GADc19OsoZeyqJ8xBwCpoZu8sqrs6ORvtiMxAAApAAA+GQb18/Hx7uzPyMJsrCEhAADTzsqKe26Dc2d2ZVk9FQaQg3ni3dk+FgbIwbtwXUxJLA9cRTNiTT1GOgxWbBVooR9klx1krQBQNyMeAAB+bV9dRzVbQitmU0VTZBNhjRtMUBA8DARGNgtPWRFegxlIQg6r0YhDLgpmmx5VahWZyG3c4tBbfRj//v9ROSpMLxWnrY5slC3U4MOMsV+gvX7GzrN3tjh+sEV0bEy82p+LhW/J4rOov4tJTwDm9NmHi2WRw12Bk1Xz+e19pUax2I+UxGZidC96uTS3yp9fUS5akwDU6MJxqCt9mk2WvGzE0q9IKh0NAAAt9cg9AAAa5klEQVR4nO1d+3/aRrYHCwkEY8AC8TAvCRwMBvOKHYgxsePETdoYe7ePdLvd9mbT7e3epNve+///cvVGc2ZGEhXdJl7OD/58EqTRaL5zzpy3IpFNUSE3v4vOzuLqpgasVobZaHayn9rUgFvaHFV7UoyLRjlJnMQ3MuCyNMsgbUSUyfY2toW2tCFqZZMaNgYhcRP4NDsJZA3IlRf98ANuaYPUT9rg6FQ+DD/iRHANyI+r4Ufc0sZIHcpRNwmhRXpRxAc828Q0t7QhquDoRNFuyAFTIw4fsVHYyES3tBEaIxydaKIVbsBSGQwo9DYz0y1tgJoyB+FJhxtxKIEBpUVzM3PdUnhq8QCdqNwJN+It3EDcaGuFfzAUFyDe0jCUSdbMEnij7QH+wdCA5O+zZagRt/z9IVNKhniHVa8m8PxG61rgzWq1mkppf5pb59zGKQv1c7ESbsB0MoxCUKjkOovxLDvaHWXPx91ecbBV9jZKxQyQvkrIAVMcEOhBDbzUID0XE+WYLCHOJCTxSbGR75baW0bfFFXHuPxN7ocdsYfvIHkS5Ca11ZklBShrzB0ol6VJbqsDbIhaDTc/ZsJp5zqpd24dUMoH0M6rxZnIQz3PTVKyfraZ2N2W4ruOzsYluxuQnKlFxsGOn7V9ry90EJ2zcTkhZEvb0MsmqL3IGF42FONy4Wwxi5qHggEgxwtDX4iaZ5Ina68IZWaVjczvP54qnd1yQpnkNsY/hfTsKJG82/NV1dRcMiDaBuKJyWBTU/zPJrXZ3Ky1G2zA9kwIjrZOEt/bGmgfLaUl6JzxJS4z2WbMfJyUmpTXY26LxRPFP3rmW/oN1B4TvvuALM5vIOlqS/9matX9bTAWlc+2Drd/A6nVVEGjfqoaXmcqEYkW65Cwfg6FmmpXSpVBu58KfquqaZ167CZVrYbYYM3UoJTrHYZfs2olDog9ZgpeaplKaryCE8sdplb2uuN8IpGo87uzRSc9YK1ACwxIjb/E2Xo5h2QhppMgsbcEP6FY4n34jqspFnrDXVEsl8VEPbvYC2LUVeO5ve5wMT/PjnbvZuPF2V4uznTqqvDJK52ymV7kxUxMeKAtbAFe5uEzJC6tRvqciNMDtvN72MAvfZyz1mhXWwUXPaCGQ9XKsFHmJWQCwHGSHBMT57kWDfO9Bjag+JRyTSVBh5KTYon8pJPb3y/t76e7s3KZZ0h9YULu7fQD/B0blj9BLZ03VpuHQ7wo9jzdfqn4Wb4hxnhZsmM3CMl8TGyMem2qxydVZwDR7CRi5qolNLzbYILiY6aDIgXwEiVtC3VA9FrusvxPKkhDdZIQUiAfhZq+VplkKIYTikmTHikO9nA1jKMkvA5gDM26NBYd5tors11tViuHY5mu1vFDYthcDOwJE+/BJENsGoHrMOSTmiouZknGacMJ0qJEubGax6+3o06Fc2fyOt7qAkyEZyYblEDikayndbcSYD4xloesArJGnaB0ALxTQ5GlWiGh3oFb1B/vZow2Hiqjfcphog7OGlTEkzl4KR3vXpJm5HPJMe3kalaG5YzHOaJXXc1JKczAexBdPVrHO1IEyQGIIqVMOgOsLOoPVc/BwmVYpim83QlK++NdkokcGDfxsQmOuC/esMTBvCw5LrKEU6FDjaeIcN1peKtdmB9tk4QIYZrqyjF/DxDKnEGU6HgP6q7/NfBWIYOWGQK9quADciNDquQA10ukkDNf5A7cjpxf/PAuxvwUaYnvusWKL97pDDkGklz663Kp9gtV1QX/YEzkVWr3zID+RMN7SLnRvv8O6l+pRjCjIbMAcpSKdxv7TwPvCNzqLFcCLAOxYIHJJNwdXb2Gt69koR/epUaA95dFl8brh3eLcjYKY1t/Ulv7w1G9odkBDf68s7IWchQo+AU+MgXvLsyuwqY9B3y6JJLnGcTv4luFhnfqDhvMxBvmf3NRKl6RLtgXkrU+cILJEvV2kETo2hY+eA+8zrLVeFnXfvfBW52Rspm3w+6Fzq2UdB6J+GR0UrIwid+RWIBcO4i3XD30glt7Wchd+2xpgJM0wzichvcEh8zEW51AjY1qG6Zm+HhobP0Qh+Vf1OyhKsJvd4l9H7zzgZxgmNrgg3eOPE8blpba7/DQ/OKQOLYGb4+IYx/bZyTe0Z4fuyZA7KXgqaq4Sej64F0BR7WJdyQNZRC1nGcArsrY8rg5Bwv0gKahl8DtidWm8sabdtSShEbue7zxbitQYHC8KZNSnQfUUDgq5002VhcE9+GrTuDt66AnDFiinI5JZbd5QOJdhXUXFt5VIHEsRQwQEOeuFP40WAOqhg60cy67eoYn3tW7QPqLgIlVb7zPCAxi5owHWaYsRXVTIU5NIPtxWHYcgbc/ZYC+k/M+ANyPLrsOfwLvEjGQhfeSMLRoGjrLetZVSvATxeXSBM92Y+qJdwmcFtqJKgi8LMHTAXukJ94FQmCIhjBf/ol/qlB5CylHyuXNnz83JktoE7w7uf034A2rKwrB3fruWyHefJooq7LwJiq4aBr6AKy72/JcAFWMI9MBinC7uDa1J97gsJDkyV46vdfpzpJu93cd90164t2B7G2mK6tfTHcunlwrCvg1qigPn90c7NRq01+NhSAAT7je5TfgjW5xcaoG1dB1z8tKR4d4R0fE5c5E76AqRrpc4BJKrt8qgHnLpIbexd9Bmrt+88K7j09NnrfMqampdi8r2JDzoIGDF95ViAg307fn8stpTcP04OKZpKzmihTlxcnFaa22Y5DB4T0oH9xcxsQbSbJEP5i5PHCkO2NwckzgeVkjnhdiND0uszrBCbxJcvDuQQYnBHoTaBGYEGqCAj00h7cXwI7CrBgvvHHRg2aY2G6lR2UjCRUBgeKFN1FslDDmkq4/udjRYNWgfX55bDG58vDkkY11rXb6/FOdnVRYnuauTqPjLYn8otvpLvgyjXUzgD2M81EP24zO9iutgl7KVmhVct0MqUs6RtJ6eBeAjCIFehsX5xyH7clDsL5RKNBL+CKjW7cK74X3PnZjBgY21eI8yUVj0OXvgbcKDh9L2/jq8sVT9PDk1IB859GzFzriVxcHNtgHpzeXL5SkoSa0oDmXXJ1tNLw5flFpqks9lF2aUIKwxGqfI1m47eYKTWx3L/sdIsbDRR0c/PHmHLyXUPlOghlARBHuVioAQy8GBfo5vsh4TMYL7x72XJ4MIaqlvHgHDUAPvNuQwwxZph7UHp1Enx6hZxcGP9denkSPJPTixGT5g5tLdCwpytPyn/QxIIO7fAkUvJHkWg01RybMEQ6L3OPhgBp1GhBHQtLhAC+8EZ9JNBrKsaNoQC2YKLADzhZgcqnweAZexirQ4BOYCeKFNx5uTVKD8zlCXfDAGx5dsoGVpqtpyD6/Vo6OLKau7dxc6xCfHJxeXCqKgpTopSbcp/oRTuwZ0dG4SLxRFvd7tgh9j9sF9gw7izp1B31jjnHAxlsqz/dKfWzMJTgaYFC0BTRwCSh00JtSx7cnqAB1nTrGS3jgjZuK6Jy1EDh54A2Lj5O6yHhlS+1Hl9Fj5fpGR/x17eD5Q0VSrrU/SEFXn77U/7f2tT5IF7qQHecRgTeH4B4tEua/GOytdIJer5WqxMIb8QtKQXMPyGugoYMgGFFPrSa9+B+yP/Cwe+ENzhF+EqgxBxvvJpA00kLf93+52bEP6kdPjo6Prm6m30Q+0RT2i6tjTYRqYF/YFxgMDhtArWZM4E34xykOtMYamWnQmqzbsoGBd/Kc6h1vA/c27nJZgiA3KVeBz0rCnIzAR8Hhjn7v8xuK31EvQFkuG2+YdBHTDZp+Q7l6bqtmO6dPosrTv0Yi3+oy/uBG09zQifPjTu0X7QYVeGTRwkaM9KeS0y1Bg66xRhEVUJxX99LxLrNyFEGaC+Y0ivRxfYzLE7e38PfkRm4+BOwgA2vZC29ibbhYvuPL42y8oe/X0CT+9kQ5Pr6+cCyvi4d5NaL+uTbVBfjp5ZEm1F/WTJts5+I7laLf5u1VJ+JjFF9jCiKTWKeyvA7utVVYKt6xLmsY4ADjZm4ZAyIqFBkFzZyyO20R+MhEoGV74T0gvQwc35hUvDmCjTd04yv6Sp3WTp9pyvf1IxvwnVcapPXvvtdkui7irxXl6NMDwxmjHIn6YQTsyxViEO8YJX2TSCFbC2/gfXP8nDS8eXYpfXMXaGwukQ0myEkUBoMqmUuzKkSxodEETMILbyLGY5CUuT2LN1m5Rx54N0HsV9b3/ysN1J1HmhIefXJqIK4d3pE/JXUv4S+Gqn5wE9VY/OLkCmmK+ov/0m5pAcScVSfyHWgWBZgeC++l2kwNigZVWv2mlWwDNJqybZBR8PZsSwU0NreGXsD3ArU9WhNadCsO3MfXgNjynv5zWqKZ/iqymO8wm+Mz8YadVTP6XP42NUT1TVRRRrriNv0sEnlfe6cd4ZUX7968Mczxh0fSkYKko8vnB6+r5DaM2VMm8KYlHROHCgWWZjzXzQoJMZPUKKMnrZ939ltL4gmOc46CNyPzxKQW8KC5jMJ9nHfpGYlAcUw6Fy0BT4lQg/DEu8CszeZ4YXRYoDI5E+8+DNPpyuvfTd1bF+qS8vCi9vpt5G1t+lp7Nsp01cgb0xqPSlF0qXvSD15p99wCOWGrJATetErSIswFgHg34xNOgLUOnByTuWEljb+bAwaJt4/1Cra+Kx8MGPllqsoXxxlRdtpyVPGNJBP5jN75Dj2PiBMnSF0aAzHxLoBNbYQqJpcvrYNbU8Yl5eT7SOSz6Y7294er42ZkqelthqH2UIlGn2mKumGRgVPUsUcY+ec4QSUU4l2alxk5XJxUhv4DNt4Z73Yz4ATm9+wfqrh2DtVrm8CWjzFUmBhhD3rjrTLCStYCyI0hGa1n4w0MDSOJ7lY5enJgs/hxQzsQ/zGdfmuArrFyr/7kkx8N99unT5ESvdmZvo8QZRaOf3kDeLfGzFx7CrHxhmYvJBB6XEV9QIY6z9g2IPBkCxoQzqWkt/vlK/oEAmS5F9h/DsM+Wb3i4r/zknJ1YdnXF9qxPXhy+o9I5JuprrfF69rZ/PYn47fnmi2uXL/7Z4T0T9ku8PB4l9BaDQjYePs2GQR71mZEFTc2uVuGlpQCLhdryxfwecTI5Di/fOQ4o9LLmVHmHBgMTLwHEG/teK3+9PLqGClPTPNbO7yr2fr/RCJvp9M32t+fvxsuI4ULk/1fXh9HpbruogG4orm1KKHxLorrFa2y8YZhVoIGuLCzXS4gs5Rd6Y7vFy5qggCyqOrkAvjWG7SQT84mAnUegflbl+fqa01UK+jY9Kl8H3n7Lz3TV/16qkEf+Wn609tIc1Y/sSzzTyUzkR+o2Bvj7xxM3/IjNt6+XrslHkuwg6LAO5Zk9i4BiclWUBQkqND8Tb71RO1J0ofF85hWsJ6+9loX1SNJeqGdzd/qcvydNljv+kA7pz+Z7mh//5qMKs8OTMSfo7pu8R7ShVlYvNtrcrcH3pzi2zgMREWsqA9+/nr1JsdDu+aeL+C7hXb4B6kPTQvUAr/V29XdZ2Bge8yo3/raEtXo6Xe6c/x9TTu2K0Iip7vQ9SP8m4PLo6jy0HKpPuL0ZTn7XfQ1lZKLzEmyEMtkYgJPVVyZeNPLADAq4PkTpssFoOF1KoDghuFywfcQ7qa1KFA9cDU9S3ohjgkOtr8FBjL17feFaY1p1rejS7694BZ6mNR0vezsnChR6cVzS4c3bDiQRmkbmeHwzhGps5zALTq9XLFUTO91xxK56Zl4s8woN+GszGX116/gb5DwiN218f2ia+jAr07xvAfEW+92MM7E2LVF7ogeG2/wqKTjX9PoRHT28mfTR6nIcnxSext5q4v72g1CSLkxLjP9LYwEsFB4k3VOgnRYcBZ8WW3nsmWgyjDxZtd1rwicwMYS4loY6S1xEx7nljSWAwcmTzv8A+KtUWF/KLNcEe6cGibeMFRh8OWrqR0XcwZ4/+Z9ZHkmKhor/zg1xfiVEn1qHOI/RoiQwGrVQ+FdAX5WTiC/tZgCBUpMvGNEbTpJIAtVFwkqHn8TPNtT4jWgeuUFHlmTqb1wg+Ot9+spDWcxmo/Vtgd0YsfHgM3JHekr9bNle7/BHvXNiVjUtTdrM5xeK5rxfbAz/TJCIuMIl1B4AyUQFM1Y1AZKFgvvQF3FcTODu20ClkewfBUnFX9meR+cc5TE9Mh6eBvXx3u7CRJyl2axZvz7SwvTz7DHTKd/11b3yg6S7pha2+lUF+c9mGXCin+vg/dyxDgkMNoo3n083YcfgKXz+7IIvpxoDJwtZepN6+JtvPXeCNZ6uZYneH6L8SxboP+IPeLbzzTL+0g6fu6ktjzTtDbuXxFiX0fRuc0GYfCGuVYiNZrZxk2McHiD1AT+sIpLePoUVtQC2gQuPhmumt+Ct3bXIWBx1wG+Tv6ajtRLE9DXxEN+MbKZnGSmk2PTSIUl0KtYQxi8YYTyjvreA/yADYl3BZsKl8fzIaWFnw0PDEhc30f0DlR+eLP6Vg1wXnWF/9bIT63rJ+/nJoNP34InfDLVhfiR7WvR1PS6salggeUq0BwGbyB7GI1RQDA1JN5VPMqF8Lxzoo7A91WwF1jQ7/HBu53vMpQGvBUCl3V+8MAbFrubq/qLmdfyCT6+bnkfPFGiyuUK8HYEdkXRqOygGgZv8N8yXRoCjgqJN1kahP3DN5GS+DSve1UYnZt88B7LsTH9A1UF7GHB+BueOGal6isT0Nr37uHfmhg/0dS0awvv6Rf6D7CAHK0kbxi8QUCa7jBpglKesHjD0iBsBp7Gt0kwN2tFHGIF1jzx1iMIKDGnCfU+dmOg85soXrZe6lddok8xBb36dc3iaUMvN/7xs/4KbaKj1Wo7huJvkDJKPb+JoyQk3l79gVidutxE9N9ziOnw8cS7b/KwlD8jXTVxvLgsiH5O8Vka8Q+jougn9/ndn393YAvxKFKuT3WTTE9tIeqzOVdTrjB4Qy2wTHFOwZ6HofH26A/kY3xbxBToAqtFrHe+ogUdJ9eHFfz5Kh56y6xe0LP++whMEBl5IOoPRgqTRt/rqL9PP5U0jC0Ov9AAvzq1Cv6LMGTpztUPgzcUrRSBXiLcDqHxJj/H7cw9kJ20z8g3QzPWHZ71Bq7dJwnRRbzg1FNUZjifyav95NnfAfpKorJxECx/eG/8/O105/XXP9XevZCcmJgBuHT1zoC7RRTlih79HdbBGzaYjcZ6uDlUPSQbD4bGmzgh4LR8CJb225Rh+nM98Aa5FpwkCrOzdC6X3uucgw60nKsO0xPvPrEhRXNpjMW1Upd2ao8UFJWuDhzAhTtjP6kzeN7J7hqOUP412BhNG9ol0pvFWworhce7xTCpghZnwr58JnnkvnvgTbZS0gS7EIsJPCGF3Mvu3Z+pQ5xYq8BY5M3UNr0evdAAf2Fz+DvzM2bqBM4I/7Z4KP85KRrlxLw0aBfag0pvLlLjweHxJspd7AECfrUXdvaxZs7OnmPjXVnj8yL1IPFQgwqEisEh+92+teHWAY9qgD88Nf/1i7k2Q2JGeO+YUHj3o6RolDJ8/i7PM5uwh8eb6JhsrQlsDcsiWrdK7Z3YydBMvJv+LUkckt15Nz79FdNEf0XpyLr7b+9cgF8oeguXg9p0+vMr89XI1rdcHtOiw+U7nFF1ZY7eqt2kDeANfcwmycxSQ0g0jY0bsa9n4l1JBE/EditNfnjD8mZ3z7zlP388cET6c4RQ/errL020qZ8zEnGXYzi8AzYXdNMG8CY7lBkvFvAb2ppYoigAXtF3D3l+F1SgJzHbwa8/MqiFicbcR5X66p8/vN7Zmep08r+TnGMRVPKka0ICSk3IfEWiuyBBUDnaBN5wOXRC58GbEMCGqrAeHJCHvpbqBqu1EDvB+yvq1MPWNWFtxtQqdejVV1/9+uuvX32+uqUwpOSOupMsDAqbjzz0aaaZ6Rzi4GwCb/WWXGQhQHqMTXFi0qwm+AZ5+lsq84y/jBPAx8DW+74Bb51U6mLMrDjt9yRqvzuow4bFu+nZLT2a6cEAxybwJoJI+pPW+GRmlUirJb774CZv/3mzF/P5vAFKHIIwrf/3S6orZpXtevScKJUX1M89F3ocdQ4ZwkUcur6kecZOQUdimghobQTvFLHJ2N4xGsGuK6v8D+rTfOLfam4ksvNSUeac0CwCfJ/IcZMhu6xuoJv0UrlxFse2ttou7ibonypLkirsBuoFi7v0EmiuPNc9Pr8H3sRXptwhoADUp3/6gkH++S3V+HAmUJMUeWFcJGVwALw1294Yj7M/GaPamRByMtvt9Iql+KBSyh12JxKrtoX2JflN1AOnunlSmnDJbNp40d8Fb5jmFdj4tmiS4d3U8Oyw05f0b4Ws6DEtkJYaHO42yoKMLL7kOL1pYIze46HzABuwUac9tmSUw9Rte6q3kml6SUeyLIrlTIyXmfoiTxNa6cfYkxPU3v9FcNH/wcVtp/OJpP2qnP61w8Tufor6bo9tvFMiPujjdfCOAGbyrS0FNNjDyCfLMQWIJfyrlXRnMcvzZTGJRrPFXpHe3UG7EI5IvSqnCXDRVkNhj2dfEiY0KKsFQLQHN+FF5GssC8XO/C4vJOp8PjvppldHFnyCs1hw0LU+Fgpc90R/zT+MVP17sW39i7Hhv89bEZ1+VVWPvBwqxRbrSbzfQNVUX3/TQsqjM9GGCNZR3v3uT/xDaOA4YbvrfQicKwf2Nn6wNM85EiAFe3OsYXx/VGR/VRo2yPSDW05/9AzQFoXbXqGpLpdqewyqbqAX6f5QM6UDB7996EOCFORrzh84dfgoJySyw7OzOfRhenrHPnJa6o2iz9dpmYISnfDfTf/DqWCWLWimCGmBBMlT/HipmQr0wUqLOFZy9EdGsDYRY+/wqvAHTe25GPAbUChZzt2LxfA6wTxSFe4LDboogIKOkuP0Gq2rP2SCdbIukv0bgXz8tGx3RGpZ+QpsoZwt3RO0Iyr7VcGniO4vqfG9XZGnBWY4JGfqi/17ZKSQjWIcEu+r7U2h5qC3yAoZQXIyxjSok5n8uAu+9/KRE/GJX5c0p7bguMfUH1R6w6ySaCQSjUZ9d97Zj7fv2xLAcJgL7tE9sDV/Ey2rzLjNR0+7LOVUPv/dowJb+vfTYCLQPEyckN3CfT8pPqzHwCepkCCm79vBtSWblqn0YlS3vqHAIb4szQ+3zH2vSS0McmdjDe7sfNiLB8qP+H9vcM8sPU/4LwAAAABJRU5ErkJggg=='},
        {'name': 'Lead & Manage', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRoM8od6IJmunYaOJz0OjfkZ8b706m8_OtjrA&s'},
    ],
    'Digital Marketing Specialist': [
        {'name': 'Market Dynamics', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTYe31IVXSI-BTXNob90d1W2x2n51effeyeAQ&s'},
        {'name': 'Digital Wizards', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUm_As-jjQdfItt575Hr1eO4mSrfZHsHftEA&s'},

    ],
    'Game Developer': [
        {'name': 'Game Dev Studio', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT09uHkEir4fhUa-NVlrqnObOZCmneFrQtQFg&s'},
        {'name': 'Playful Designs', 'image': 'https://i.pinimg.com/736x/0a/d9/4e/0ad94e37ba50e3923a0e067b20bfe99c.jpg'},

    ],
}


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def documentation(request):
    return render(request, 'documentation.html')


def find_jobs(request):
    if request.method == 'POST':
        user_skills = request.POST.get('skills', '').split(',')
        user_skills = [skill.strip().lower() for skill in user_skills]  # Convert user skills to lowercase

        matching_jobs = []
        for job in job_data:
            job_skills = [skill.lower() for skill in job['skills']]  # Convert job skills to lowercase

            # Count matches using lowercase skills
            skill_match_count = sum(1 for skill in user_skills if skill in job_skills)
            match_percentage = (skill_match_count / len(job['skills'])) * 100 if job['skills'] else 0

            if skill_match_count > 0:
                matching_jobs.append({
                    'job': job,
                    'match_percentage': round(match_percentage),
                    'companies': companies_ready_to_hire.get(job['title'], [])
                })

        return render(request, 'job_results.html', {'jobs': matching_jobs})

    return render(request, 'index.html')

def index(request):
    return render(request, 'index.html', {'user': request.user})

def digital_assistance(request):
    return render(request, 'digital assistance.html')
# Login view


def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = UserRegistrationForm()
    return render(request, 'signup.html', {'form': form})