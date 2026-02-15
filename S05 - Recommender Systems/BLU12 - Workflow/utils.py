def make_user_features_lfm(user_id: list, df):
    """
    Construct the csr matrix of user features for lightFM prediction.
    """
    new_user_data=df[df.user_id.isin(user_id)]
    # transform the item id to internal ids
    new_user_data.loc[:,['item_id_int']]=new_user_data.recipe_id.map(item_id_map)
    # transform user id for input into predict method
    new_user_data.loc[:,['user_id_int']]=new_user_data.user_id.map(
        dict(zip(user_id,range(len(user_id)))))
    
    # construct the item features matrix
    new_user_features=np.zeros([len(user_id),num_items])
    new_user_features[new_user_data['user_id_int'].to_numpy(),
                      new_user_data['item_id_int'].to_numpy()]=new_user_data.rating
    
    return csr_matrix(new_user_features)