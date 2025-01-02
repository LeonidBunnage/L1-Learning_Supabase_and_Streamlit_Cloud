import os
import supabase

# class SupabaseService:
#     def __init__(self, url: str, api_key: str):
#         self.url = url
#         self.api_key = api_key
#         self._initiate_client()

#     def _initiate_client(self):
#         self.client = supabase.create_client(self.url, self.api_key)

# Supabase Testing
## Creating the client
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase_client = supabase.create_client(supabase_url, supabase_key)