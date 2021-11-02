#### Adding objects
For `adding` objects to the database, run on Heroku console:
```
python manage.py shell
$ from pwapp.models import table
$ t = table(text="Text here")
$ t.save()
```
For `deleting` objects:
```
$ table.objects.filter(text="Text here").delete()
```


#### Icons
To change the default icons, create a `static` folder in the project root directory, inside it add another folder `images`. Inside this folder add the directory `icons`. Finally, add the icons you want your app to serve. 
It is recommended that you use a name format that includes the dimensions of the icon (ex: `icon-512x512.png` for a 512px icon).
For each icon you add, make sure you add it in the `settings.py` to the `PWA_APP_ICONS` list:
```
PWA_APP_ICONS = [
    {
        'src': '/static/images/icons/icon-192x192.png',
        'sizes': '192x192',
        'type': 'image/png',
    },
    {
        'src': '/static/images/icons/icon-512x512.png',
        'sizes': '512x512',
        'type': 'image/png',
    }
]
```
For more customization check the [pwa app used in this project](https://github.com/silviolleite/django-pwa)
