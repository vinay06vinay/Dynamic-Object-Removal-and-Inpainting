import os
import cv2
import numpy as np
from skimage.metrics import structural_similarity

def compute_psnr(original_img, reconstructed_img):
    psnr = cv2.PSNR(original_img, reconstructed_img)
    return psnr

def compute_ssim(original_img, reconstructed_img):
    gray_original = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
    gray_reconstructed = cv2.cvtColor(reconstructed_img, cv2.COLOR_BGR2GRAY)
    
    _, ssim_score = structural_similarity(gray_original, gray_reconstructed, full=True)
    return ssim_score
    return ssim_score

def compute_metrics(gt_folder, inpainted_folder):
    psnr_values = []
    ssim_values = []

    for frame_name in os.listdir(gt_folder):
        gt_frame = cv2.imread(os.path.join(gt_folder, frame_name))
        inpainted_frame = cv2.imread(os.path.join(inpainted_folder, frame_name))

        assert gt_frame.shape == inpainted_frame.shape, "Frames must have the same dimensions"
        assert gt_frame.dtype == inpainted_frame.dtype, "Frames must have the same data type"

        psnr = compute_psnr(gt_frame, inpainted_frame)
        ssim_score = compute_ssim(gt_frame, inpainted_frame)

        psnr_values.append(psnr)
        ssim_values.append(ssim_score)

    average_psnr = np.mean(psnr_values)
    average_ssim = np.mean(ssim_values)

    print(f'Average PSNR: {average_psnr}')
    print(f'Average SSIM: {average_ssim}')

# Usage:
gt_folder = 'customgtf1'
inpainted_folder = 'customf_inpainted'

compute_metrics(gt_folder, inpainted_folder)
