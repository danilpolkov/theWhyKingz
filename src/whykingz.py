def approximate_function(t: int, A: float, h: float) -> float:
    
    '''
    функция для аппроксимации retention
    
    Параметры:
    ----------------
    t: int
        переменная
        
    A: float
        коэфициент в знаменателе 
        
    h: float
        коэфициент возле переменной
        
    возвращает значение функции
        
    '''
    
    return 1/(h*t + A)


def median_confident_interval(data: pd.Series, ci: float = .95, p = .5) -> list:
    
    '''
    функция которая считает доверительный интервал для персентиля 
    
    Параметры:
    -------------
    data 
        ряд
        
    ci: 
        доверительный интервал
        
    p: float
        персентиль
    
    возвращает list и снижней и верхней границей
    '''
    
    data = data.values

    data = data.reshape(-1)
    data = np.sort(data)
    N = data.shape[0]

    lowCount, upCount = stats.binom.interval(ci, N, p, loc=0)
    lowCount -= 1
    return data[int(lowCount)], data[int(upCount)]


def compare_groups(df: pd.DataFrame, feature_name: str, target_feature: str = 'loyal_user'):
    
    '''
    выводит название фичи
    выводит граничные значения которые отсекли аномальные наблюдения, отсекается .05 персентись с обоих сторон
    выводит доверительные интервалы для медианны для фичи для 2х категорий пользователей
    отображает 2 графика
    1) информативная часть с распределениями фичи в зависимости от группы пользователей
    2) полсные распределениями фичи в зависимости от группы пользователей
    
    Параметры:
    -------------
    df: pd.DataFrame
        датафрейм с параметром и таргет фичей
    
    feature_name: str
        фича которую анализируем
    
    target_feature: str
        таргет фича по которой можно разделить наблюдения на группы
    
    '''
    
    print('-'*20, 'feature name:', feature_name, '-'*20)
    
    # убираем аномальные наблюдения
    lower_bound = df[feature_name].quantile(.05)
    upper_bound = df[feature_name].quantile(.95)
    short_df =  df[(df[feature_name] <= upper_bound)
                   & (df[feature_name] >= lower_bound)][[feature_name, target_feature]]

    print(f'lower_bound:', lower_bound, 
          f'\nupper_bound:' , upper_bound)
    
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
    fig.set_size_inches(14, 6)
        
    # тут лучше переписать в более универсальный вариант
    class_colour = {0:'r', 1:'b'}
    class_naming = {0:'unloyal', 1:'loyal'}
    for class_id in [0, 1]:
        subset = short_df[short_df[target_feature] == class_id][feature_name]
        sns.distplot(subset, hist=False, kde=True, norm_hist=True, label=class_naming[class_id], color=class_colour[class_id],
                     ax=ax1).set_title('informative interval', fontsize=16)


    for class_id in [0, 1]:
        subset = user_df[user_df['loyal_user'] == class_id][feature_name]
        sns.distplot(subset, hist=False, kde=True, norm_hist=True, label=class_naming[class_id], color=class_colour[class_id],
                     ax=ax2).set_title('full interval', fontsize=16)

    print(f'confident interval for median in loyal group:', 
          median_confident_interval(user_df.loc[user_df[target_feature] == 1, feature_name], 0.95, 0.5))
    print(f'confident interval for median in unloyal group:',
          median_confident_interval(user_df.loc[user_df[target_feature] == 0, feature_name], 0.95, 0.5))
          