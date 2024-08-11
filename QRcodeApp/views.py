from django.shortcuts import render
from django.http import JsonResponse
import qrcode
from io import BytesIO
import base64

def index(request):
    return render(request, "index.html")

def generateQR(request):
    if request.method == "POST":
        link = request.POST.get('link')  # Ensure the key matches the one used in FormData
        print("Received Link: ", link)
        if link:
            try:
                # Object QR
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                # Make Qr code
                qr.add_data(link)
                qr.make(fit=True)
                
                img = qr.make_image(fill='black', back_color='white')
                buffer = BytesIO()
                img.save(buffer)  # Save image without specifying format
                img_str = base64.b64encode(buffer.getvalue()).decode()

                return JsonResponse({'qr_code': f'data:image/png;base64,{img_str}'})

            except Exception as e:
                print(f"Error generating QR code: {e}")
                return JsonResponse({'error': 'Error generating QR code'}, status=500)
        else:
            return JsonResponse({'error': 'No link provided'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
