from PIL import Image, ImageEnhance

# open image
im = Image.open("MonaLisa_orig.jpg")
size = 30,30

thumbnail = True
hicontrast = True
kidpix = True

if(thumbnail):
    # save thumbnail
    thumb = im.copy()
    thumb.thumbnail(size)
    thumb.save("MonaLisa_thumb.jpg","JPEG")

if(hicontrast or kidpix):
    contraster = ImageEnhance.Contrast(im)
    conim = contraster.enhance(2.0)

    if(hicontrast):
        # save hi contrast version
        conim.save("MonaLisa_hicon.jpg","JPEG")
    if(kidpix):
        conim.thumbnail(size)
        conim.save("MonaLisa_kidpix.jpg","JPEG")
