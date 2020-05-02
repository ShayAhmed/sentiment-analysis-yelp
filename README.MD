1. Run py -m pip install -r req.txt
2. Run get_reviews.py OR Run load_save_review_data.ipynb
    This will save all of the data in the /data folder, its around 6 gb
3. Run separate_by_business_id.ipynb (Optional, very time-intensive)
4. Run load_save_restaurant_business_data.ipynb- saves CSV of relevant information for all restaurant businesses in dataset (used to cross-reference with CSV of reviews from load_save_review_data.ipynb)
5. Run get_restaurant_review.ipynb- saves CSV of JUST restaurant reviews (subset of result from step 2)
