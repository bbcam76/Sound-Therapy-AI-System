class AIRecommender:
    def __init__(self, user_preferences):
        self.user_preferences = user_preferences

    def analyze_preferences(self):
        # Analyze user preferences to determine suitable sound therapy options
        # This is a placeholder for the actual analysis logic
        recommended_sounds = []
        if self.user_preferences.get('stress_level') > 5:
            recommended_sounds.append('calming_music')
        if self.user_preferences.get('focus_level') < 3:
            recommended_sounds.append('focus_sounds')
        return recommended_sounds

    def recommend(self):
        # Generate recommendations based on analyzed preferences
        recommendations = self.analyze_preferences()
        return recommendations

# Example usage:
# user_preferences = {'stress_level': 6, 'focus_level': 2}
# recommender = AIRecommender(user_preferences)
# print(recommender.recommend())  # Output: ['calming_music', 'focus_sounds']