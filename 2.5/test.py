# Обучение логистической регрессии с кросс-валидацией
logistic_model = LogisticRegression(max_iter=1000, random_state=42)
cv_scores_logistic = cross_val_score(logistic_model, features_train, target_train, cv=5, scoring='roc_auc')
print(f"Average ROC AUC score for Logistic Regression: {np.mean(cv_scores_logistic):.4f}")

# Обучаем модель на полном наборе
logistic_model.fit(features_train, target_train)

# Предсказание и оценка
y_pred_logistic = logistic_model.predict_proba(features_test)[:, 1]
roc_auc_logistic = roc_auc_score(target_test, y_pred_logistic)
print(f"ROC AUC score for Logistic Regression on test set: {roc_auc_logistic:.4f}")

# Топ-10 признаков по важности (коэффициенты логистической регрессии)
importance_logistic = pd.Series(np.abs(logistic_model.coef_[0]), index=X.columns)
top10_logistic = importance_logistic.nlargest(10)
print("Top 10 важнейших признаков для логистической регрессии:")
print(top10_logistic)

# Визуализация важности признаков
plt.figure(figsize=(10, 6))
top10_logistic.plot(kind='barh')
plt.title('Топ-10 признаков по важности (Логистическая регрессия)')
plt.show()