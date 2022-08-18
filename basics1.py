import cv2

img = cv2.imread('files/lena.jpg',0)

print(img)

cv2.imshow("resim",img)

# fonksiyonun hemen kapanmaması için bir algoritma
# esc -> 27 çıkış yapar // s -> resmi kaydedip çıkar
key = cv2.waitKey(0) & 0xFF
if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite("files/lena_copy.jpg",img)
    cv2.destroyAllWindows()