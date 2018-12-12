# Generated by Django 2.0.5 on 2018-09-12 06:57

from django.db import migrations


def seed(apps, schema_editor):
    Artist = apps.get_model('tunr', 'Artist')
    Song = apps.get_model('tunr', 'Song')

    sigur_ros = Artist(name="Sigur Ros", nationality="Icelandic", photo_url="https://d14wch1fpzoq5q.cloudfront.net/2017/11/19222455/sigur-ros-crop.jpg")
    aix_em_klemm = Artist(name="Aix Em Klemm", nationality="United States", photo_url="http://bornmusic.org/blog/wp-content/uploads/2012/03/awingedvictoryforthesullen_blog_436.jpg")
    alaskan_tapes = Artist(name="Alaskan Tapes", nationality="Canadian", photo_url="https://f4.bcbits.com/img/0013651310_10.jpg")
    brian_eno = Artist(name="Brian Eno", nationality="British", photo_url="https://cps-static.rovicorp.com/3/JPG_400/MI0004/412/MI0004412130.jpg?partner=allrovi.com")
    big_freedia = Artist(name="Big Freedia", nationality="USA", photo_url="https://www.billboard.com/files/media/Big-Freedia-getty-portrait-2015-a-billboard-1548.jpg")
    mono = Artist(name="Mono", nationality="Japanese", photo_url="https://www.scenewave.com/wp-content/uploads/mono-japan.jpg")
    orchid = Artist(name="Orchid", nationality="USA", photo_url="https://www.metal-archives.com/images/3/5/4/0/3540297397_photo.jpg?4958")

    sigur_ros.save()
    aix_em_klemm.save()
    alaskan_tapes.save()
    brian_eno.save()
    big_freedia.save()
    mono.save()
    orchid.save()

    ny_batteri = Song(title="Ný batterí", album="Ágætis byrjun", preview_url="https://open.spotify.com/track/1O3g5Z3mZkQ5ud460FWeDE?si=uM24oytrTgKS2-Mwqp1Fqw", artist=sigur_ros)
    tgwtfcc = Song(title="The Girl With The Flesh Colored Crayon", album="Aix Em Klemm", preview_url="https://open.spotify.com/track/2RWxRXIiwbcKEaplXoplUv?si=HowxQAXqTW6rnvB77airHQ", artist=aix_em_klemm)
    all_was_quiet = Song(title="All Was Quiet", album="You Were Always An Island", preview_url="https://open.spotify.com/track/3dW7J5pJFu0nE4eGtmcqey?si=hPXBr9tvT5605_jGLTW60g", artist=alaskan_tapes)
    discreet_music = Song(title="Discreet Music", album="Discreet Music", preview_url="https://open.spotify.com/track/69eD0IfAqEIUnKX63Npksy?si=7pz1q45dShGTBQUwY8rzjQ", artist=brian_eno)
    explode = Song(title="Explode", album="Just Be Free", preview_url="https://open.spotify.com/track/7CMfPwodyj6K2Envg1qxWa?si=xF6wSQ76RwGe-iVQOCEA0g", artist=big_freedia)
    pure_as_snow = Song(title="Pure As Snow(Trails of the Winter Storm", album="Hymn To The Immortal Wind", preview_url="https://open.spotify.com/track/1zPMPIE1nc3ee6THnbjoYA?si=1JRQfGR8QLyQV6OAlqdGog", artist=mono)
    cosmonaut_of_three = Song(title="Cosmonaut of Three", album="Capricorn", preview_url="https://open.spotify.com/track/08Q0xzywnSDECAmxSitPMz?si=dRspb4BBShK-90SVXHtTyA", artist=orchid)

    ny_batteri.save()
    tgwtfcc.save()
    all_was_quiet.save()
    discreet_music.save()
    explode.save()
    pure_as_snow.save()
    cosmonaut_of_three.save()

def fallow(apps, schema_editor):
    Artist = apps.get_model('tunr', 'Artist')
    Song = apps.get_model('tunr', 'Song')
    Song.objects.all().delete()
    Artist.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('tunr', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed, fallow)
    ]