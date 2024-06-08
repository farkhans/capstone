def filepath(instance, filename):
    extension = filename.split('.')[-1]
    return f"profile-img-{instance.username}.{extension}"