from launch.ad_virality import pick_promotion_type, score_ad

class PromotionStrategy:
    def plan(self, ad_content):
        promotion_type = pick_promotion_type(ad_content)
        virality_score = score_ad(ad_content)
        return {
            "ad_content": ad_content,
            "promotion_type": promotion_type,
            "virality_score": virality_score
        }
