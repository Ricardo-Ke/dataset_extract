import os

test_size_all_1 = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
test_size_all = [0.3]
out_put_path = './'
out_put_file_name = os.path.join(out_put_path ,'/hin_apcpa_classify_score.txt')
out_put_file = open(out_put_file_name, 'w')

for test_size in test_size_all:

    X, y = np.split(self.aa_apcpa_vector_label, (128,), axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1, test_size=test_size)

    line = str(test_size) + '\n'

    apcpa_svc = svm.SVC(kernel='rbf', gamma=0.07, C=2)
    apcpa_svc.fit(X_train, y_train.ravel())

    # print '基于APCPA的HIN-accurcy'
    # print '基于APCPA的HIN-accurcy:训练集' + str(apcpa_svc.score(X_train, y_train))
    # line += '基于APCPA的HIN-accurcy:训练集' + str(apcpa_svc.score(X_train, y_train)) + '\n'
    # print '基于APCPA的HIN-accurcy:测试集' + str(apcpa_svc.score(X_test, y_test))
    # line += '基于APCPA的HIN-accurcy:测试集' + str(apcpa_svc.score(X_test, y_test)) + '\n'

    y_train_pred = apcpa_svc.predict(X_train)
    y_test_pred = apcpa_svc.predict(X_test)

    # print '基于APCPA的HIN-召回率'
    # train_recall = str(recall_score(y_train, y_train_pred, average='macro'))
    # print '基于APCPA的HIN-召回率:训练集' + train_recall
    # line += '基于APCPA的HIN-召回率:训练集' + train_recall + '\n'
    # test_recall = str(recall_score(y_test, y_test_pred, average='macro'))
    # print '基于APCPA的HIN-召回率:测试集' + test_recall
    # line += '基于APCPA的HIN-召回率:测试集' + test_recall + '\n'
    #
    # print '基于APCPA的HIN-micro-f1'
    # print '基于APCPA的HIN-micro-f1:训练集' + str(f1_score(y_train, y_train_pred, average='micro'))
    # line += '基于APCPA的HIN-micro-f1:训练集' + str(f1_score(y_train, y_train_pred, average='micro')) + '\n'
    # print '基于APCPA的HIN-micro-f1:测试集' + str(f1_score(y_test, y_test_pred, average='micro'))
    # line += '基于APCPA的HIN-micro-f1:测试集' + str(f1_score(y_test, y_test_pred, average='micro')) + '\n'
    #
    # print '基于APCPA的HIN-macro-f1'
    # print '基于APCPA的HIN-macro-f1:训练集' + str(f1_score(y_train, y_train_pred, average='macro'))
    # line += '基于APCPA的HIN-macro-f1:训练集' + str(f1_score(y_train, y_train_pred, average='macro')) + '\n'
    # print '基于APCPA的HIN-macro-f1:测试集' + str(f1_score(y_test, y_test_pred, average='macro'))
    # line += '基于APCPA的HIN-macro-f1:测试集' + str(f1_score(y_test, y_test_pred, average='macro')) + '\n'

    print '基于APCPA的HIN-精确率:训练集' + str(precision_score(y_train, y_train_pred, average='weighted', labels=np.unique(y_train_pred)))
    print '基于APCPA的HIN-精确率:测试集' + str(precision_score(y_test, y_test_pred, average='weighted', labels=np.unique(y_test_pred)))